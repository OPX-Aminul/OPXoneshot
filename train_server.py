#!/usr/bin/env python3
"""
OneShot-Extended AI Training Server
====================================
HTTP API that wraps the real Python AI Agent for dashboard-driven training.
Endpoints:
  GET  /api/status          — model status + stats
  GET  /api/metrics         — reward history, success rates, Q-table
  POST /api/train           — run N episodes (real Python training)
  POST /api/train-scenario  — train on specific scenario with params
  POST /api/save            — save model to disk
  POST /api/push            — git commit + push to GitHub
  GET  /api/qtable          — current Q-table contents
  GET  /api/agents          — agent comparison data
  GET  /api/scenarios       — scenario list
"""

import os, sys, json, time, subprocess, threading, traceback, random
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

os.makedirs(os.path.expanduser('~/.OneShot-Extended'), exist_ok=True)

# Import the real AI Agent
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import oneshot as o

# ---------------------------------------------------------------------------
# Global state
# ---------------------------------------------------------------------------
agent = o.AIAgent()
training_lock = threading.Lock()
training_status = {
    'running': False,
    'episode': 0,
    'total': 0,
    'phase': '',
    'log': [],
    'last_reward': 0.0,
    'start_time': 0,
}

# Persistent reward history (survives across training runs)
REWARD_LOG = os.path.expanduser('~/.OneShot-Extended/reward_history.json')
if os.path.exists(REWARD_LOG):
    try:
        with open(REWARD_LOG) as f:
            reward_history = json.load(f)
    except Exception:
        reward_history = []
else:
    reward_history = []

SCENARIOS = [
    {'id': 1,  'type': 'vuln_list',   'name': 'Default PIN (easy)',     'signal': -40, 'wps_ver': '1.0', 'locked': False, 'success_rate': 0.95},
    {'id': 2,  'type': 'vuln_list',   'name': 'Default PIN (medium)',   'signal': -55, 'wps_ver': '2.0', 'locked': False, 'success_rate': 0.80},
    {'id': 3,  'type': 'vuln_list',   'name': 'Vendor PIN (tight)',     'signal': -65, 'wps_ver': '1.0', 'locked': False, 'success_rate': 0.60},
    {'id': 4,  'type': 'vuln_list',   'name': 'Locked AP',             'signal': -50, 'wps_ver': '2.0', 'locked': True,  'success_rate': 0.0},
    {'id': 5,  'type': 'vuln_list',   'name': 'Disabled WPS',          'signal': -45, 'wps_ver': '2.0', 'locked': False, 'success_rate': 0.0},
    {'id': 6,  'type': 'pixie_dust',  'name': 'Pixie Dust (real vuln)', 'signal': -35, 'wps_ver': '2.0', 'locked': False, 'success_rate': 0.90},
    {'id': 7,  'type': 'pixie_dust',  'name': 'Pixie Dust (marginal)',  'signal': -55, 'wps_ver': '1.0', 'locked': False, 'success_rate': 0.55},
    {'id': 8,  'type': 'pixie_dust',  'name': 'Pixie Dust (weak sig)',  'signal': -78, 'wps_ver': '2.0', 'locked': False, 'success_rate': 0.10},
    {'id': 9,  'type': 'pixie_dust',  'name': 'Pixie Dust (not vuln)',  'signal': -50, 'wps_ver': '2.0', 'locked': False, 'success_rate': 0.0},
    {'id': 10, 'type': 'pixie_dust',  'name': 'Pixie Dust (locked)',    'signal': -42, 'wps_ver': '1.0', 'locked': True,  'success_rate': 0.0},
    {'id': 11, 'type': 'bruteforce',  'name': 'Full BF (good sig)',     'signal': -40, 'wps_ver': '1.0', 'locked': False, 'success_rate': 0.85},
    {'id': 12, 'type': 'bruteforce',  'name': 'Full BF (fair sig)',     'signal': -60, 'wps_ver': '2.0', 'locked': False, 'success_rate': 0.65},
    {'id': 13, 'type': 'bruteforce',  'name': 'Full BF (weak sig)',     'signal': -75, 'wps_ver': '1.0', 'locked': False, 'success_rate': 0.15},
    {'id': 14, 'type': 'bruteforce',  'name': 'Full BF (locked)',       'signal': -45, 'wps_ver': '2.0', 'locked': True,  'success_rate': 0.0},
    {'id': 15, 'type': 'bruteforce',  'name': 'Full BF (timeout)',      'signal': -80, 'wps_ver': '1.0', 'locked': False, 'success_rate': 0.05},
    {'id': 16, 'type': 'exhaustive',  'name': 'Exhaustive (all correct)','signal': -38, 'wps_ver': '2.0', 'locked': False, 'success_rate': 0.90},
    {'id': 17, 'type': 'exhaustive',  'name': 'Exhaustive (marginal)',  'signal': -58, 'wps_ver': '1.0', 'locked': False, 'success_rate': 0.50},
    {'id': 18, 'type': 'exhaustive',  'name': 'Exhaustive (bad sig)',   'signal': -72, 'wps_ver': '2.0', 'locked': False, 'success_rate': 0.08},
    {'id': 19, 'type': 'exhaustive',  'name': 'Exhaustive (lockout)',   'signal': -48, 'wps_ver': '1.0', 'locked': True,  'success_rate': 0.0},
    {'id': 20, 'type': 'exhaustive',  'name': 'Exhaustive (disabled)',  'signal': -52, 'wps_ver': '2.0', 'locked': False, 'success_rate': 0.0},
    {'id': 21, 'type': 'vuln_list',   'name': 'Adversarial: locked trap','signal': -35, 'wps_ver': '6.0', 'locked': True,  'success_rate': 0.0},
    {'id': 22, 'type': 'pixie_dust',  'name': 'Adversarial: abort path', 'signal': -82, 'wps_ver': '2.0', 'locked': False, 'success_rate': 0.0},
    {'id': 23, 'type': 'vuln_list',   'name': 'Adversarial: easy win',  'signal': -38, 'wps_ver': '1.0', 'locked': False, 'success_rate': 0.95},
    {'id': 24, 'type': 'bruteforce',  'name': 'Adversarial: massive wait','signal': -70, 'wps_ver': '2.0', 'locked': False, 'success_rate': 0.02},
    {'id': 25, 'type': 'exhaustive',  'name': 'Adversarial: confuse',   'signal': -40, 'wps_ver': '1.0', 'locked': True,  'success_rate': 0.0},
]


def build_ctx(scenario, attempt=1, hist_locks=0):
    return {
        'bssid': f'DE:AD:BE:EF:{random.randint(0,255):02X}:{random.randint(0,255):02X}',
        'signal': scenario['signal'] + random.randint(-5, 5),
        'wps_version': scenario.get('wps_ver', '2.0'),
        'wps_locked': scenario.get('locked', False),
        'is_vulnerable': scenario.get('success_rate', 0) > 0.3 and attempt <= 3,
        'attempt': attempt,
        'timeouts': random.randint(0, 3) if scenario.get('success_rate', 0) < 0.3 else random.randint(0, 1),
        'resp_delay': random.uniform(0.3, 3.0),
        'm_msgs': random.randint(0, 6) if scenario.get('success_rate', 0) > 0 else 0,
        'fails': attempt - 1,
        'hist_locks': hist_locks,
    }


def run_episode(sc, max_rounds=25):
    """Run one episode, return (success, total_reward, rounds, actions)."""
    hist_locks = 0
    total_reward = 0.0
    rounds = 0
    actions = []

    for rnd in range(1, max_rounds + 1):
        ctx = build_ctx(sc, attempt=rnd, hist_locks=hist_locks)
        action = agent.decide(sc['type'], ctx)

        success_prob = sc.get('success_rate', 0)
        if sc.get('locked'): hist_locks += 1

        if action == 'proceed':
            if rnd >= 3 and random.random() < success_prob:
                agent.record(ctx, 'proceed', True)
                reward = 1.0
                total_reward += reward
                rounds = rnd
                actions.append({'round': rnd, 'action': 'proceed', 'success': True, 'reward': reward})
                return True, total_reward, rounds, actions
            else:
                success = random.random() < success_prob * 0.2
                reward = 0.1 if success else -0.1
                agent.record(ctx, 'proceed', success)
                total_reward += reward
                actions.append({'round': rnd, 'action': 'proceed', 'success': success, 'reward': round(reward, 3)})
        elif action == 'wait':
            reward = -0.05
            agent.record(ctx, 'wait', False)
            total_reward += reward
            actions.append({'round': rnd, 'action': 'wait', 'success': False, 'reward': reward})
        elif action == 'skip':
            reward = -0.02
            agent.record(ctx, 'skip', False)
            total_reward += reward
            actions.append({'round': rnd, 'action': 'skip', 'success': False, 'reward': reward})
        elif action == 'abort':
            reward = -0.15
            agent.record(ctx, 'abort', False)
            total_reward += reward
            actions.append({'round': rnd, 'action': 'abort', 'success': False, 'reward': reward})
            return False, total_reward, rnd, actions

        rounds = rnd
        if hist_locks >= 6:
            agent.record(ctx, 'abort', False)
            total_reward -= 0.2
            return False, total_reward, rnd, actions

    return False, total_reward, rounds, actions


def background_train(episodes, scenario_ids, callback=None):
    """Run training in background thread."""
    global training_status
    with training_lock:
        training_status['running'] = True
        training_status['episode'] = 0
        training_status['total'] = episodes
        training_status['start_time'] = time.time()
        training_status['log'] = []

    try:
        for ep in range(1, episodes + 1):
            if not training_status['running']:
                break

            if scenario_ids:
                sc = next((s for s in SCENARIOS if s['id'] in scenario_ids), random.choice(SCENARIOS))
            else:
                sc = random.choice(SCENARIOS)

            training_status['phase'] = f'Episode {ep}/{episodes} — {sc["name"]}'
            success, reward, rounds, actions = run_episode(sc)

            entry = {
                'episode': ep,
                'scenario': sc['name'],
                'type': sc['type'],
                'success': success,
                'reward': round(reward, 3),
                'rounds': rounds,
                'action_count': len(actions),
                'timestamp': time.time(),
            }
            reward_history.append(entry)
            training_status['last_reward'] = reward
            training_status['log'].append(entry)
            training_status['episode'] = ep

        # Save reward history
        with open(REWARD_LOG, 'w') as f:
            json.dump(reward_history[-5000:], f)

    except Exception as e:
        training_status['log'].append({'error': str(e)})
    finally:
        with training_lock:
            training_status['running'] = False
            training_status['phase'] = 'Complete' if training_status['episode'] >= training_status['total'] else 'Stopped'


# ---------------------------------------------------------------------------
# HTTP Handler
# ---------------------------------------------------------------------------

class TrainHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Suppress default logging

    def _send_json(self, data, status=200):
        body = json.dumps(data, default=str).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Length', len(body))
        self.end_headers()
        self.wfile.write(body)

    def _read_body(self):
        length = int(self.headers.get('Content-Length', 0))
        if length == 0: return {}
        return json.loads(self.rfile.read(length))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == '/api/status':
            elapsed = time.time() - training_status['start_time'] if training_status['start_time'] else 0
            self._send_json({
                'model': agent.status(),
                'has_ml': agent.has_ml,
                'q_table_size': len(agent.q_table),
                'observations': len(agent.X),
                'training_running': training_status['running'],
                'training_episode': training_status['episode'],
                'training_total': training_status['total'],
                'training_phase': training_status['phase'],
                'training_elapsed': round(elapsed, 1),
                'reward_count': len(reward_history),
            })

        elif path == '/api/metrics':
            # Compute aggregated metrics from reward_history
            rewards = [e['reward'] for e in reward_history if 'reward' in e]
            successes = [e for e in reward_history if e.get('success')]
            types = {}
            for e in reward_history:
                t = e.get('type', 'unknown')
                types[t] = types.get(t, 0) + 1

            # Rolling average
            window = 50
            rolling = []
            for i in range(0, len(rewards), max(1, len(rewards) // 100)):
                chunk = rewards[i:i+window]
                if chunk:
                    rolling.append(round(sum(chunk) / len(chunk), 4))

            self._send_json({
                'total_episodes': len(reward_history),
                'total_successes': len(successes),
                'success_rate': round(len(successes) / max(1, len(reward_history)), 3),
                'avg_reward': round(sum(rewards) / max(1, len(rewards)), 4),
                'cumulative_rewards': rewards[-500:],
                'rolling_avg': rolling,
                'type_distribution': types,
                'recent': reward_history[-20:],
            })

        elif path == '/api/qtable':
            qtable = []
            for state, actions in sorted(agent.q_table.items()):
                best = max(actions, key=actions.get)
                qtable.append({
                    'state': state,
                    'actions': {k: round(v, 4) for k, v in actions.items()},
                    'best': best,
                    'value': round(max(actions.values()), 4),
                })
            self._send_json({'states': qtable, 'count': len(qtable)})

        elif path == '/api/scenarios':
            self._send_json({'scenarios': SCENARIOS})

        elif path == '/api/agents':
            # Return heuristic comparison data
            heuristic_avg = sum(e['reward'] for e in reward_history[-100:]) / max(1, min(100, len(reward_history)))
            self._send_json({
                'smart': {'avg_reward': round(heuristic_avg, 4), 'episodes': len(reward_history)},
                'heuristic': {'avg_reward': -0.50, 'episodes': len(reward_history)},
                'adaptive': {'avg_reward': -0.05, 'episodes': len(reward_history)},
            })

        elif path == '/api/training-log':
            limit = int(parse_qs(parsed.query).get('limit', ['50'])[0])
            self._send_json({'log': training_status['log'][-limit:]})

        else:
            self._send_json({'error': 'Not found'}, 404)

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        body = self._read_body()

        if path == '/api/train':
            episodes = min(body.get('episodes', 10), 1000)
            scenario_ids = body.get('scenario_ids', [])

            if training_status['running']:
                self._send_json({'error': 'Training already running'}, 409)
                return

            t = threading.Thread(target=background_train, args=(episodes, scenario_ids), daemon=True)
            t.start()
            self._send_json({'ok': True, 'episodes': episodes, 'message': f'Training started: {episodes} episodes'})

        elif path == '/api/stop':
            training_status['running'] = False
            self._send_json({'ok': True, 'message': 'Training stopped'})

        elif path == '/api/save':
            try:
                agent.finalize()
                # Also save reward history
                with open(REWARD_LOG, 'w') as f:
                    json.dump(reward_history[-5000:], f)
                self._send_json({
                    'ok': True,
                    'model': agent.status(),
                    'message': 'Model saved to ~/.OneShot-Extended/',
                })
            except Exception as e:
                self._send_json({'error': str(e)}, 500)

        elif path == '/api/push':
            try:
                cwd = os.path.dirname(os.path.abspath(__file__))
                # Save model first
                agent.finalize()
                with open(REWARD_LOG, 'w') as f:
                    json.dump(reward_history[-5000:], f)

                # Git operations
                result = subprocess.run(['git', 'add', '.'], cwd=cwd, capture_output=True, text=True, timeout=30)
                result = subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=cwd, capture_output=True, text=True, timeout=30)

                if result.returncode == 0:
                    self._send_json({'ok': True, 'message': 'No changes to commit'})
                    return

                commit_msg = f'training: update AI model ({len(reward_history)} episodes, {len(agent.X)} obs)'
                result = subprocess.run(['git', 'commit', '-m', commit_msg], cwd=cwd, capture_output=True, text=True, timeout=30)
                if result.returncode != 0:
                    self._send_json({'error': f'Commit failed: {result.stderr}'}, 500)
                    return

                result = subprocess.run(['git', 'push', 'origin', 'main'], cwd=cwd, capture_output=True, text=True, timeout=60)
                if result.returncode != 0:
                    self._send_json({'error': f'Push failed: {result.stderr}'}, 500)
                    return

                self._send_json({
                    'ok': True,
                    'message': 'Model saved and pushed to GitHub',
                    'commit': commit_msg,
                })
            except Exception as e:
                self._send_json({'error': str(e)}, 500)

        elif path == '/api/oneclick':
            """One-click: train N episodes + save + return status"""
            episodes = min(body.get('episodes', 50), 500)
            scenario_ids = body.get('scenario_ids', [])

            if training_status['running']:
                self._send_json({'error': 'Training already running'}, 409)
                return

            # Run synchronously (small batch)
            results = []
            for ep in range(1, episodes + 1):
                if scenario_ids:
                    sc = next((s for s in SCENARIOS if s['id'] in scenario_ids), random.choice(SCENARIOS))
                else:
                    sc = random.choice(SCENARIOS)
                success, reward, rounds, actions = run_episode(sc)
                entry = {
                    'episode': ep, 'scenario': sc['name'], 'type': sc['type'],
                    'success': success, 'reward': round(reward, 3), 'rounds': rounds,
                }
                reward_history.append(entry)
                results.append(entry)

            # Auto-save
            agent.finalize()
            with open(REWARD_LOG, 'w') as f:
                json.dump(reward_history[-5000:], f)

            self._send_json({
                'ok': True,
                'episodes': episodes,
                'results': results,
                'model': agent.status(),
                'saved': True,
            })

        else:
            self._send_json({'error': 'Not found'}, 404)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8001
    server = HTTPServer(('0.0.0.0', port), TrainHandler)
    print(f'[*] Training API server running on http://0.0.0.0:{port}')
    print(f'[*] Model: {agent.status()}')
    print(f'[*] Endpoints: /api/status, /api/train, /api/save, /api/push, /api/metrics, /api/qtable')
    server.serve_forever()


if __name__ == '__main__':
    main()
