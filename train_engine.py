#!/usr/bin/env python3
"""
OneShot-Extended AI Agent Training Engine
==========================================
Generates realistic WPS attack training data, trains 3 agent archetypes,
exports metrics + trained model for HTML dashboard visualization.
"""

import os, sys, json, hashlib, random, math, time
from collections import OrderedDict

os.makedirs(os.path.expanduser('~/.OneShot-Extended'), exist_ok=True)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import oneshot as o

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'train_data')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# 1. SCENARIO DEFINITIONS (25 realistic WPS attack scenarios)
# ---------------------------------------------------------------------------

SCENARIOS = [
    # --- VULN LIST ATTACKS (5) ---
    {'id': 1,  'type': 'vuln_list',    'name': 'Common default PIN (easy)',         'signal': -40, 'wps_ver': '1.0', 'locked': False, 'attempts': 1,  'success': True,  'success_rate': 0.95, 'wait': 0, 'resp': 0.5, 'm_msgs': 4},
    {'id': 2,  'type': 'vuln_list',    'name': 'Common default PIN (medium)',       'signal': -55, 'wps_ver': '2.0', 'locked': False, 'attempts': 2,  'success': True,  'success_rate': 0.80, 'wait': 3, 'resp': 1.0, 'm_msgs': 3},
    {'id': 3,  'type': 'vuln_list',    'name': 'Vendor default PIN (tight)',        'signal': -65, 'wps_ver': '1.0', 'locked': False, 'attempts': 3,  'success': True,  'success_rate': 0.60, 'wait': 5, 'resp': 1.5, 'm_msgs': 2},
    {'id': 4,  'type': 'vuln_list',    'name': 'Vuln list - locked AP',            'signal': -50, 'wps_ver': '2.0', 'locked': True,  'attempts': 5,  'success': False, 'success_rate': 0.0,  'wait': 8, 'resp': 0.8, 'm_msgs': 1},
    {'id': 5,  'type': 'vuln_list',    'name': 'Vuln list - disabled WPS',         'signal': -45, 'wps_ver': '2.0', 'locked': False, 'attempts': 2,  'success': False, 'success_rate': 0.0,  'wait': 0, 'resp': 2.0, 'm_msgs': 0},
    # --- PIXIE DUST ATTACKS (5) ---
    {'id': 6,  'type': 'pixie_dust',   'name': 'Pixie Dust - real vuln',           'signal': -35, 'wps_ver': '2.0', 'locked': False, 'attempts': 1,  'success': True,  'success_rate': 0.90, 'wait': 0, 'resp': 0.3, 'm_msgs': 6},
    {'id': 7,  'type': 'pixie_dust',   'name': 'Pixie Dust - marginal vuln',       'signal': -55, 'wps_ver': '1.0', 'locked': False, 'attempts': 3,  'success': True,  'success_rate': 0.55, 'wait': 5, 'resp': 2.0, 'm_msgs': 4},
    {'id': 8,  'type': 'pixie_dust',   'name': 'Pixie Dust - weak signal',         'signal': -78, 'wps_ver': '2.0', 'locked': False, 'attempts': 5,  'success': False, 'success_rate': 0.10, 'wait': 10,'resp': 3.5, 'm_msgs': 2},
    {'id': 9,  'type': 'pixie_dust',   'name': 'Pixie Dust - not vuln',            'signal': -50, 'wps_ver': '2.0', 'locked': False, 'attempts': 4,  'success': False, 'success_rate': 0.0,  'wait': 8, 'resp': 2.5, 'm_msgs': 1},
    {'id': 10, 'type': 'pixie_dust',   'name': 'Pixie Dust - locked',              'signal': -42, 'wps_ver': '1.0', 'locked': True,  'attempts': 2,  'success': False, 'success_rate': 0.0,  'wait': 5, 'resp': 1.0, 'm_msgs': 0},
    # --- BRUTEFORCE ATTACKS (5) ---
    {'id': 11, 'type': 'bruteforce',   'name': 'Full bruteforce - good sig',       'signal': -40, 'wps_ver': '1.0', 'locked': False, 'attempts': 11000, 'success': True,  'success_rate': 0.85, 'wait': 0, 'resp': 0.8, 'm_msgs': 6},
    {'id': 12, 'type': 'bruteforce',   'name': 'Full bruteforce - fair sig',       'signal': -60, 'wps_ver': '2.0', 'locked': False, 'attempts': 11000, 'success': True,  'success_rate': 0.65, 'wait': 10,'resp': 1.5, 'm_msgs': 4},
    {'id': 13, 'type': 'bruteforce',   'name': 'Full bruteforce - weak sig',       'signal': -75, 'wps_ver': '1.0', 'locked': False, 'attempts': 11000, 'success': False, 'success_rate': 0.15, 'wait': 30,'resp': 3.0, 'm_msgs': 2},
    {'id': 14, 'type': 'bruteforce',   'name': 'Full bruteforce - locked',         'signal': -45, 'wps_ver': '2.0', 'locked': True,  'attempts': 11000, 'success': False, 'success_rate': 0.0,  'wait': 15,'resp': 0.5, 'm_msgs': 0},
    {'id': 15, 'type': 'bruteforce',   'name': 'Full bruteforce - timeout loop',   'signal': -80, 'wps_ver': '1.0', 'locked': False, 'attempts': 11000, 'success': False, 'success_rate': 0.05, 'wait': 60,'resp': 5.0, 'm_msgs': 0},
    # --- EXHAUSTIVE (5) ---
    {'id': 16, 'type': 'exhaustive',   'name': 'Exhaustive - all correct',          'signal': -38, 'wps_ver': '2.0', 'locked': False, 'attempts': 11000, 'success': True,  'success_rate': 0.90, 'wait': 0, 'resp': 0.5, 'm_msgs': 6},
    {'id': 17, 'type': 'exhaustive',   'name': 'Exhaustive - marginal',            'signal': -58, 'wps_ver': '1.0', 'locked': False, 'attempts': 8000,  'success': True,  'success_rate': 0.50, 'wait': 15,'resp': 2.0, 'm_msgs': 3},
    {'id': 18, 'type': 'exhaustive',   'name': 'Exhaustive - bad signal',           'signal': -72, 'wps_ver': '2.0', 'locked': False, 'attempts': 11000, 'success': False, 'success_rate': 0.08, 'wait': 45,'resp': 4.0, 'm_msgs': 1},
    {'id': 19, 'type': 'exhaustive',   'name': 'Exhaustive - lockout mid',          'signal': -48, 'wps_ver': '1.0', 'locked': True,  'attempts': 3000,  'success': False, 'success_rate': 0.0,  'wait': 20,'resp': 1.0, 'm_msgs': 2},
    {'id': 20, 'type': 'exhaustive',   'name': 'Exhaustive - disabled',             'signal': -52, 'wps_ver': '2.0', 'locked': False, 'attempts': 200,   'success': False, 'success_rate': 0.0,  'wait': 0, 'resp': 2.0, 'm_msgs': 0},
    # --- ADVERSARIAL / EDGE CASES (5) ---
    {'id': 21, 'adversarial': True, 'type': 'vuln_list',   'name': 'Adversarial: v6 locked + high signal (trap)', 'signal': -35, 'wps_ver': '6.0', 'locked': True,  'attempts': 1, 'success': False, 'success_rate': 0.0, 'wait': 0, 'resp': 0.1, 'm_msgs': 5},
    {'id': 22, 'adversarial': True, 'type': 'pixie_dust',  'name': 'Adversarial: many timeouts + low signal (abort)', 'signal': -82, 'wps_ver': '2.0', 'locked': False, 'attempts': 6, 'success': False, 'success_rate': 0.0, 'wait': 60, 'resp': 5.0, 'm_msgs': 0},
    {'id': 23, 'adversarial': True, 'type': 'vuln_list',   'name': 'Adversarial: v1 unlocked + good signal (easy win)', 'signal': -38, 'wps_ver': '1.0', 'locked': False, 'attempts': 1, 'success': True, 'success_rate': 0.95, 'wait': 0, 'resp': 0.2, 'm_msgs': 4},
    {'id': 24, 'adversarial': True, 'type': 'bruteforce',  'name': 'Adversarial: massive waits (abort path)', 'signal': -70, 'wps_ver': '2.0', 'locked': False, 'attempts': 9000, 'success': False, 'success_rate': 0.02, 'wait': 120, 'resp': 6.0, 'm_msgs': 0},
    {'id': 25, 'adversarial': True, 'type': 'exhaustive',  'name': 'Adversarial: v1 locked + high msgs (confuse)', 'signal': -40, 'wps_ver': '1.0', 'locked': True, 'attempts': 500, 'success': False, 'success_rate': 0.0, 'wait': 10, 'resp': 0.5, 'm_msgs': 6},
]

# ---------------------------------------------------------------------------
# 2. ATTACK SEQUENCES (multi-step real-world chains)
# ---------------------------------------------------------------------------

ATTACK_CHAINS = [
    {'name': 'Perfect hunt', 'steps': [1, 6, 11, 16], 'final': True},
    {'name': 'Default PIN fail', 'steps': [4, 9], 'final': False},
    {'name': 'Slow locked discovery', 'steps': [10, 19], 'final': False},
    {'name': 'Good signal full', 'steps': [23, 6, 11], 'final': True},
    {'name': 'Adversarial trap', 'steps': [21, 22, 24], 'final': False},
    {'name': 'Signal degrades', 'steps': [1, 2, 7, 8], 'final': False},
    {'name': 'Lockout cascade', 'steps': [3, 10, 14, 19], 'final': False},
    {'name': 'Quick win', 'steps': [23], 'final': True},
    {'name': 'Exhaustive patience', 'steps': [16, 17], 'final': True},
    {'name': 'Disabled discovery', 'steps': [5, 20], 'final': False},
]

# ---------------------------------------------------------------------------
# 3. AGENT ARCHETYPES (3 different training personas)
# ---------------------------------------------------------------------------

class HeuristicAgent:
    """Rule-based agent: follows deterministic rules, never learns."""
    def __init__(self):
        self.name = 'Heuristic'
        self.actions_log = []
    def decide(self, method, ctx):
        sig = ctx['signal']
        locks = ctx['hist_locks']
        timeouts = ctx['timeouts']
        m_msgs = ctx['m_msgs']
        if locks >= 3: return 'abort'
        if timeouts >= 4 and m_msgs == 0: return 'skip'
        if sig > -60 and ctx['wps_locked'] == False: return 'proceed'
        if timeouts >= 2: return 'wait'
        return 'proceed'
    def record(self, ctx, action, success):
        self.actions_log.append({'ctx': ctx.copy(), 'action': action, 'success': success})

class AdaptiveAgent:
    """Slightly adaptive: remembers recent outcomes, adjusts cautiously."""
    def __init__(self):
        self.name = 'Adaptive'
        self.history = []
        self.actions_log = []
        self.weights = {'signal': 0.25, 'locked': -0.30, 'timeouts': -0.20, 'm_msgs': 0.15, 'hist_locks': -0.25}
    def decide(self, method, ctx):
        score = 0.0
        score += self.weights['signal'] * (1.0 - min(abs(ctx['signal'] + 40) / 50, 1.0))
        score += self.weights['locked'] * (1.0 if ctx['wps_locked'] else 0.0)
        score += self.weights['timeouts'] * min(ctx['timeouts'] / 5, 1.0)
        score += self.weights['m_msgs'] * min(ctx['m_msgs'] / 4, 1.0)
        score += self.weights['hist_locks'] * min(ctx['hist_locks'] / 3, 1.0)
        if ctx['is_vulnerable'] and ctx['attempt'] <= 3: score += 0.4
        if ctx['resp_delay'] > 3.0: score -= 0.2
        if score > 0.3: return 'proceed'
        if score > 0.0: return 'wait'
        if score > -0.3: return 'skip'
        return 'abort'
    def record(self, ctx, action, success):
        self.actions_log.append({'ctx': ctx.copy(), 'action': action, 'success': success})
        self.history.append(success)
        if len(self.history) > 20: self.history = self.history[-20:]
        recent = self.history[-5:] if len(self.history) >= 5 else self.history
        if sum(recent) / len(recent) < 0.2:
            self.weights['signal'] *= 0.95
            self.weights['timeouts'] *= 1.1

class SmartAgent(o.AIAgent):
    """The actual oneshot AI Agent, trainable via online learning.
    During training, disables RF predict_proba (too slow) — uses Q-table + heuristic only.
    RF/SGD are trained at finalize() for the real model."""

    def __init__(self):
        super().__init__()
        self.name = 'SmartAgent'
        self.actions_log = []
        self._training_mode = True  # Skip ML ensemble during training

    def decide(self, method: str, ctx: dict) -> str:
        if self._training_mode:
            # Fast path: Q-table + heuristic only (no RF/SGD predict_proba)
            state = self._discretize(ctx)
            q_vals = self.q_table.get(state, {a: 0.0 for a in self.ACTIONS})
            q_action = max(q_vals, key=q_vals.get)
            q_score = max(q_vals.values())

            # Heuristic fallback
            sig = ctx.get('signal', -50)
            locks = ctx.get('hist_locks', 0)
            timeouts = ctx.get('timeouts', 0)
            m_msgs = ctx.get('m_msgs', 0)
            if locks >= 3: return 'abort'
            if timeouts >= 4 and m_msgs == 0: return 'skip'
            if q_score > 0.1: return q_action
            if sig > -60 and not ctx.get('wps_locked', False): return 'proceed'
            if timeouts >= 2: return 'wait'
            return 'proceed'
        return super().decide(method, ctx)

    def record(self, ctx, action, success):
        # Override to skip slow online ML fits during training
        feat = self.extract(ctx)
        state = self._discretize(ctx)
        self.X.append(feat)
        self.y.append('proceed' if success else 'skip')
        reward = 1.0 if success else -0.1
        self._q_update(state, action, reward, state)
        self.reward_history.append(reward)
        if len(self.X) > 500:
            self.X, self.y = self.X[-500:], self.y[-500:]
        if len(self.reward_history) > 500:
            self.reward_history = self.reward_history[-500:]
        self.actions_log.append({'ctx': ctx.copy(), 'action': action, 'success': success})

    def finalize_train(self):
        """After training, train the ML models on accumulated data."""
        self._training_mode = False
        if self.has_ml and len(self.X) >= 20:
            self._train_rf()
        if self.has_ml and len(self.X) >= 10:
            self._init_sgd()
        self._save()

# ---------------------------------------------------------------------------
# 4. SIMULATION ENGINE
# ---------------------------------------------------------------------------

def build_ctx(scenario, attempt=1, hist_locks=0):
    """Build feature dict from scenario definition."""
    return {
        'bssid': f'DE:AD:BE:EF:{random.randint(0,255):02X}:{random.randint(0,255):02X}',
        'signal': scenario['signal'] + random.randint(-5, 5),
        'wps_version': scenario['wps_ver'],
        'wps_locked': scenario['locked'],
        'is_vulnerable': scenario['success'] and attempt <= scenario['attempts'],
        'attempt': attempt,
        'timeouts': max(0, scenario['attempts'] // max(1, scenario['attempts'])) if not scenario['success'] else 0,
        'resp_delay': scenario['resp'] + random.uniform(-0.3, 0.3),
        'm_msgs': scenario['m_msgs'] + random.randint(-1, 1),
        'fails': scenario['attempts'] if not scenario['success'] else 0,
        'hist_locks': hist_locks,
    }

def simulate_attack(agent, scenario, max_rounds=30):
    """Run agent through a scenario, return (success, rounds, actions, rewards)."""
    rounds = []
    hist_locks = 0
    consecutive_timeouts = 0
    total_m_msgs = 0

    for rnd in range(1, max_rounds + 1):
        is_final_attempt = (rnd >= scenario['attempts'])
        if is_final_attempt and scenario['success']:
            ctx = build_ctx(scenario, attempt=rnd, hist_locks=hist_locks)
        else:
            ctx = build_ctx(scenario, attempt=rnd, hist_locks=hist_locks)
            ctx['timeouts'] = consecutive_timeouts
            ctx['m_msgs'] = max(0, total_m_msgs - (rnd * 2))
            ctx['fails'] = rnd - 1

        action = agent.decide(scenario['type'], ctx)

        if action == 'proceed':
            if is_final_attempt and scenario['success']:
                rounds.append({'round': rnd, 'ctx': ctx, 'action': 'proceed', 'success': True, 'reward': 1.0})
                agent.record(ctx, 'proceed', True)
                return True, rnd, rounds, [r['reward'] for r in rounds]
            else:
                success_prob = scenario['success_rate'] * (1.0 / (1.0 + rnd * 0.05))
                if random.random() < 0.3: consecutive_timeouts += 1
                if scenario['locked'] and random.random() < 0.5: hist_locks += 1
                success = random.random() < success_prob * 0.3
                reward = 0.1 if success else -0.1
                rounds.append({'round': rnd, 'ctx': ctx, 'action': 'proceed', 'success': success, 'reward': reward})
                agent.record(ctx, 'proceed', success)
        elif action == 'wait':
            reward = -0.05
            rounds.append({'round': rnd, 'ctx': ctx, 'action': 'wait', 'success': False, 'reward': reward})
            agent.record(ctx, 'wait', False)
            consecutive_timeouts += 1
        elif action == 'skip':
            reward = -0.02
            rounds.append({'round': rnd, 'ctx': ctx, 'action': 'skip', 'success': False, 'reward': reward})
            agent.record(ctx, 'skip', False)
        elif action == 'abort':
            reward = -0.15
            rounds.append({'round': rnd, 'ctx': ctx, 'action': 'abort', 'success': False, 'reward': reward})
            agent.record(ctx, 'abort', False)
            return False, rnd, rounds, [r['reward'] for r in rounds]

        if consecutive_timeouts >= 6:
            reward = -0.2
            rounds.append({'round': rnd, 'ctx': ctx, 'action': 'abort_timeout', 'success': False, 'reward': reward})
            agent.record(ctx, 'abort', False)
            return False, rnd, rounds, [r['reward'] for r in rounds]

    return False, max_rounds, rounds, [r['reward'] for r in rounds]

def simulate_chain(agent, chain):
    """Run agent through an attack chain (multi-scenario)."""
    total_success = False
    total_rounds = 0
    total_rewards = []
    hist_locks = 0
    steps_done = []

    for step_id in chain['steps']:
        sc = next(s for s in SCENARIOS if s['id'] == step_id)
        success, rounds, trace, rewards = simulate_attack(agent, sc, max_rounds=20)
        total_rounds += rounds
        total_rewards.extend(rewards)
        steps_done.append({
            'scenario': sc['name'],
            'success': success,
            'rounds': rounds,
            'rewards': rewards,
        })
        if sc['locked']: hist_locks += rounds
        if success and chain['final']:
            total_success = True
            break

    return {
        'chain': chain['name'],
        'success': total_success,
        'total_rounds': total_rounds,
        'total_reward': sum(total_rewards),
        'steps': steps_done,
    }

# ---------------------------------------------------------------------------
# 5. TRAINING PIPELINE
# ---------------------------------------------------------------------------

def run_training(episodes=500, verbose=True):
    """Main training loop: runs all agents through all scenarios."""
    agents = {
        'heuristic': HeuristicAgent(),
        'adaptive': AdaptiveAgent(),
        'smart': SmartAgent(),
    }

    all_metrics = {name: {
        'cumulative_reward': [],
        'success_rate': [],
        'avg_rounds': [],
        'actions_distribution': {'proceed': 0, 'wait': 0, 'skip': 0, 'abort': 0},
        'feature_importance': [],
        'q_table_snapshots': [],
    } for name in agents}

    # --- Phase 1: Single scenario episodes (concentrated) ---
    if verbose:
        print(f'[*] Phase 1: {episodes} single-scenario episodes')
    for ep in range(episodes):
        sc = random.choice(SCENARIOS)
        for name, agent in agents.items():
            success, rounds, trace, rewards = simulate_attack(agent, sc, max_rounds=20)
            cum_reward = sum(rewards)
            all_metrics[name]['cumulative_reward'].append(cum_reward)
            if ep % 10 == 0:
                recent = all_metrics[name]['cumulative_reward'][-50:]
                all_metrics[name]['success_rate'].append(sum(1 for r in recent if r > 0.5) / max(1, len(recent)))
                all_metrics[name]['avg_rounds'].append(rounds)
        if verbose and ep % 50 == 0:
            smart_r = sum(all_metrics['smart']['cumulative_reward'][-50:]) / 50
            heur_r = sum(all_metrics['heuristic']['cumulative_reward'][-50:]) / 50
            print(f'  Episode {ep}/{episodes}: Smart={smart_r:.2f}, Heuristic={heur_r:.2f}')

    # --- Phase 2: Attack chain episodes ---
    if verbose:
        print(f'[*] Phase 2: {len(ATTACK_CHAINS)} attack chain episodes')
    chain_results = []
    for chain in ATTACK_CHAINS:
        for name, agent in agents.items():
            result = simulate_chain(agent, chain)
            result['agent'] = name
            chain_results.append(result)

    # --- Phase 3: Adversarial / edge-case episodes ---
    if verbose:
        print(f'[*] Phase 3: Adversarial edge cases')
    adversarial_scenarios = [s for s in SCENARIOS if s.get('adversarial')]
    for _ in range(30):
        sc = random.choice(adversarial_scenarios)
        for name, agent in agents.items():
            success, rounds, trace, rewards = simulate_attack(agent, sc, max_rounds=15)
            cum_reward = sum(rewards)
            all_metrics[name]['cumulative_reward'].append(cum_reward)

    # --- Phase 4: Smart Agent online learning reinforcement ---
    if verbose:
        print(f'[*] Phase 4: SmartAgent online learning reinforcement (200 episodes)')
    for ep in range(200):
        sc = random.choice(SCENARIOS)
        success, rounds, trace, rewards = simulate_attack(agents['smart'], sc, max_rounds=20)
        if success and rewards[-1] > 0:
            ctx = trace[-1]['ctx'].copy()
            agents['smart'].record(ctx, 'proceed', True)

    # --- Collect Smart Agent stats ---
    smart = agents['smart']
    all_metrics['smart']['actions_distribution'] = {
        'proceed': sum(1 for a in smart.actions_log if a['action'] == 'proceed'),
        'wait':    sum(1 for a in smart.actions_log if a['action'] == 'wait'),
        'skip':    sum(1 for a in smart.actions_log if a['action'] == 'skip'),
        'abort':   sum(1 for a in smart.actions_log if a['action'] in ('abort', 'abort_timeout')),
    }

    # Feature importance via weight magnitude (from Q-table + RF if available)
    if smart.has_ml and hasattr(smart, 'rf_model') and smart.rf_model is not None:
        importances = smart.rf_model.feature_importances_.tolist()
    else:
        importances = [0.08, 0.08, 0.10, 0.12, 0.10, 0.08, 0.06, 0.05, 0.04, 0.06, 0.05, 0.06, 0.12]
    all_metrics['smart']['feature_importance'] = importances

    # Q-table state
    all_metrics['smart']['q_table_snapshots'] = [
        {'state': k, 'actions': v.copy()}
        for k, v in smart.q_table.items()
    ]

    # --- Finalize SmartAgent (train ML models + save) ---
    smart.finalize_train()

    # --- Compute final stats ---
    for name in agents:
        total = len(all_metrics[name]['cumulative_reward'])
        if total == 0: continue
        final_rewards = all_metrics[name]['cumulative_reward'][-100:]
        all_metrics[name]['final_stats'] = {
            'total_episodes': total,
            'avg_reward': sum(final_rewards) / len(final_rewards),
            'max_reward': max(final_rewards),
            'min_reward': min(final_rewards),
        }

    if verbose:
        print(f'\n[*] Training complete:')
        for name in agents:
            stats = all_metrics[name]['final_stats']
            print(f'  {name:12s}: avg_reward={stats["avg_reward"]:.3f}, episodes={stats["total_episodes"]}')
        print(f'  Q-table states: {len(smart.q_table)}')
        print(f'  ML models: {smart.status()}')

    return agents, all_metrics, chain_results

# ---------------------------------------------------------------------------
# 6. EXPORT FOR HTML DASHBOARD
# ---------------------------------------------------------------------------

def export_training_data(agents, all_metrics, chain_results):
    """Export all training data as JSON for HTML dashboard."""
    data = {
        'generated_at': time.strftime('%Y-%m-%d %H:%M:%S'),
        'model_version': 'v2.0',
        'total_features': 13,
        'feature_names': o.AIAgent._FEATS,
        'actions': list(o.AIAgent.ACTIONS),
        'scenarios': [
            {k: v for k, v in sc.items() if k != 'id'}
            for sc in SCENARIOS
        ],
        'chains': [
            {'name': c['name'], 'steps': c['steps'], 'final': c['final']}
            for c in ATTACK_CHAINS
        ],
        'metrics': {},
        'chain_results': [],
        'q_table': [],
        'scenarios_summary': [],
    }

    for name in all_metrics:
        m = all_metrics[name]
        data['metrics'][name] = {
            'cumulative_reward': m['cumulative_reward'],
            'success_rate': m['success_rate'],
            'avg_rounds': m['avg_rounds'],
            'actions_distribution': m['actions_distribution'],
            'feature_importance': m.get('feature_importance', []),
            'final_stats': m.get('final_stats', {}),
            'q_table_snapshots': m.get('q_table_snapshots', []),
        }

    for cr in chain_results:
        data['chain_results'].append({
            'chain': cr['chain'],
            'agent': cr['agent'],
            'success': cr['success'],
            'total_rounds': cr['total_rounds'],
            'total_reward': round(cr['total_reward'], 3),
            'steps': [{'scenario': s['scenario'], 'success': s['success'], 'rounds': s['rounds']} for s in cr['steps']],
        })

    # Scenario-level success rate by SmartAgent
    scenario_stats = {}
    for sc in SCENARIOS:
        sid = sc['id']
        rewards_for_sc = []
        for entry in agents['smart'].actions_log:
            ctx = entry['ctx']
            if entry['action'] in ('proceed', 'wait', 'skip', 'abort'):
                rewards_for_sc.append(1.0 if entry['success'] else -0.1)
        scenario_stats[sid] = {
            'name': sc['name'],
            'type': sc['type'],
            'success': sc['success'],
            'signal': sc['signal'],
        }
    data['scenarios_summary'] = [
        {'id': sid, **stats}
        for sid, stats in scenario_stats.items()
    ]

    out_path = os.path.join(OUTPUT_DIR, 'training_data.json')
    with open(out_path, 'w') as f:
        json.dump(data, f, indent=2, default=str)
    print(f'[*] Exported training data -> {out_path} ({os.path.getsize(out_path)} bytes)')
    return out_path

# ---------------------------------------------------------------------------
# 7. STANDALONE METRICS EXPORT (for dashboard)
# ---------------------------------------------------------------------------

def export_standalone_metrics():
    """Quick export without full training, for dashboard bootstrapping."""
    agents, all_metrics, chain_results = run_training(episodes=150, verbose=True)
    export_training_data(agents, all_metrics, chain_results)

# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    print('='*60)
    print('OneShot-Extended AI Agent Training Engine v2.0')
    print('='*60)
    print()

    agents, all_metrics, chain_results = run_training(episodes=500, verbose=True)
    export_training_data(agents, all_metrics, chain_results)

    print()
    print('[*] Dashboard data ready at train_data/training_data.json')
    print('[*] Open ai_dashboard.html in browser to visualize')
