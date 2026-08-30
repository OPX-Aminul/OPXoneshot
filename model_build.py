#!/usr/bin/env python3
"""Standalone golden-model trainer for the Community Learning Sync System.

This script is intended to run in CI (`.github/workflows/nightly-model-build.yml`)
to periodically rebuild the shared community model from Supabase and publish it
back to the repo. It is also runnable locally.

Hard-coded Supabase defaults (overridable via env — plan \u00a73/\u00a732 forbid
committing privileged secrets, so we use os.environ.get with safe anon default):
"""
import os
import sys
import json
import time
import shutil
import urllib.request
import urllib.parse
import urllib.error

# --- Supabase config (env-overridable, plan \u00a73/\u00a732) ------------------------
# CI must inject SUPABASE_SERVICE_ROLE_KEY (privileged, cross-user read). Never
# hardcode the service_role key here. Falls back to the public anon key which
# only permits the owner's own rows.
SUPABASE_URL = os.environ.get('SUPABASE_URL', 'https://oenckshhftqjjwhngxzo.supabase.co')
SUPABASE_KEY = os.environ.get(
    'SUPABASE_KEY',
    os.environ.get(
        'SUPABASE_SERVICE_ROLE_KEY',
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJl'
        'ZiI6Im9lbmNrc2hoZnRxamp3aG5neHpvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3'
        'ODc4MDkzNzYsImV4cCI6MjEwMzM4NTM3Nn0.xetav4AA9f3Vr6TjWcLtejCBboZ'
        'KwrTg3DTEj00TkRo'))
API = f'{SUPABASE_URL}/rest/v1/training_data'
HEADERS = {'apikey': SUPABASE_KEY, 'Authorization': f'Bearer {SUPABASE_KEY}'}

# --- safety constants (mirror oneshot.py) -----------------------------------
FOOTPRINT_WARN = 80 * 1024 * 1024
FOOTPRINT_CRIT = 90 * 1024 * 1024
FOOTPRINT_HARD = 0  # disabled — models grow freely via Releases
MAX_EVENTS_PER_REQ = 50
MAX_PULL_ROWS = 20000
MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
META_PATH = os.path.join(MODEL_DIR, 'model_metadata.json')


def _http_request(url, data=None, headers=None, method='GET'):
    headers = headers or {}
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                body = resp.read().decode()
                return body, resp
        except urllib.error.HTTPError as e:
            if attempt < 3:
                time.sleep(2.0 * (attempt + 1))
                continue
            raise
        except Exception:
            if attempt < 3:
                time.sleep(2.0 * (attempt + 1))
                continue
            raise
    raise RuntimeError('http retry exhausted')


def validate_event(ev):
    try:
        sig = float(ev.get('signal'))
        rew = float(ev.get('reward'))
    except (TypeError, ValueError):
        return False
    if not (isinstance(sig, float) and sig == sig and abs(sig) < 1e9):
        return False
    if not (isinstance(rew, float) and rew == rew and abs(rew) <= 1e6):
        return False
    if ev.get('success') not in (True, False, 0, 1):
        return False
    if ev.get('action') not in ('proceed', 'skip', 'wait', 'abort'):
        return False
    return True


def quality_score(ev):
    try:
        sig = max(-100.0, min(0.0, float(ev.get("signal"))))
        rew = max(-1.0, min(1.0, float(ev.get("reward"))))
    except (TypeError, ValueError):
        return 0.0
    s = (sig + 100.0) / 100.0
    return max(0.0, min(1.0, 0.5 * s + 0.5 * max(0.0, rew)))


def model_footprint():
    total = 0
    for base in (os.path.expanduser('~/.OneShot-Extended'), MODEL_DIR):
        if not os.path.isdir(base):
            continue
        for root, _, files in os.walk(base):
            for fn in files:
                fp = os.path.join(root, fn)
                try:
                    total += os.path.getsize(fp)
                except OSError:
                    pass
    return total


def read_metadata():
    try:
        with open(META_PATH) as f:
            return json.load(f)
    except Exception:
        return {'model_version': 'v0.0.0'}


def write_metadata(meta):
    os.makedirs(MODEL_DIR, exist_ok=True)
    tmp = META_PATH + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(meta, f, indent=2)
    os.replace(tmp, META_PATH)


def bump_version(meta):
    v = meta.get('model_version', 'v0.0.0')
    try:
        nums = [int(x) for x in v.lstrip('v').split('.')]
        while len(nums) < 3:
            nums.append(0)
        nums[2] += 1
        if nums[2] > 99:
            nums[2] = 0
            nums[1] += 1
        if nums[1] > 99:
            nums[1] = 0
            nums[0] += 1
        return dict(meta, model_version=f'v{nums[0]}.{nums[1]}.{nums[2]}')
    except Exception:
        return dict(meta, model_version='v0.0.1')


def pull_rows(limit=MAX_PULL_ROWS):
    rows = []
    offset = 0
    while len(rows) < limit:
        params = {
            'select': 'id,event_id,ts,user_id,signal,locked,action,success,reward,profile,bssid,essid,pin,firmware,chipset,mac',
            'order': 'id.desc',
            'limit': str(min(MAX_EVENTS_PER_REQ * 5, 2000)),
            'offset': str(offset),
        }
        q = urllib.parse.urlencode(params)
        body, _ = _http_request(f'{API}?{q}', headers=HEADERS, method='GET')
        chunk = json.loads(body)
        if not chunk:
            break
        rows.extend(chunk)
        offset += len(chunk)
        if len(chunk) < params['limit']:
            break
        if len(rows) >= limit:
            break
    return rows


def main():
    try:
        import joblib
        import numpy as np
    except ImportError:
        print('[model_build] scikit-learn/joblib required', file=sys.stderr)
        sys.exit(2)

    print('[model_build] Pulling community rows from Supabase...')
    try:
        rows = pull_rows()
    except Exception as e:
        print(f'[model_build] pull failed: {e}', file=sys.stderr)
        sys.exit(3)

    X, y = [], []
    seen = set()
    for r in rows:
        if not validate_event(r):
            continue
        eid = r.get('event_id')
        if eid and eid in seen:
            continue
        if eid:
            seen.add(eid)
        feat = [
            float(r.get('signal') or -50),
            1.0 if r.get('locked') else 0.0,
            float(r.get('attempt', 1)),
            float(r.get('m_msgs', 3 if r.get('success') else 0)),
            float(r.get('fails', 0 if r.get('success') else 1)),
            # ADVANCEMENT 3: Expanded features (with safe defaults)
            float(r.get('chip_id', 0)) / 7.0,
            float(r.get('channel_congestion', 0.0)),
            (float(r.get('noise_floor', -90.0)) + 100.0) / 100.0,
            # NEW: Device identity features for richer model learning
            # chipset as hash bucket (0-6): broadcom=0, mediatek=1, realtek=2, atheros=3, qualcomm=4, other=5, unknown=6
            {'broadcom': 0.0, 'mediatek': 1.0, 'realtek': 2.0, 'atheros': 3.0, 'qualcomm': 4.0}.get(
                (r.get('chipset') or '').lower().split()[0] if r.get('chipset') else '', 6.0) / 6.0,
            # pin length as feature (8-digit=1.0, 7-digit=0.875, empty=0.0)
            len(str(r.get('pin', '') or '')) / 8.0 if r.get('pin') else 0.0,
            # has_bssid as binary feature (known target = 1.0)
            1.0 if r.get('bssid') else 0.0,
        ]
        X.append(feat)
        y.append('proceed' if r.get('success') else 'skip')

    if len(X) < 20:
        print(f'[model_build] not enough valid rows ({len(X)}); skipping', file=sys.stderr)
        sys.exit(0)

    Xa = np.array(X)
    ya = np.array(y)

    from sklearn.ensemble import RandomForestClassifier
    rf = RandomForestClassifier(n_estimators=150, max_depth=12,
                                min_samples_leaf=2, n_jobs=-1)
    rf.fit(Xa, ya)

    # Quality gate (plan \u00a77): only publish if model is sufficiently informative
    from sklearn.model_selection import cross_val_score
    score = float(cross_val_score(rf, Xa, ya, cv=3, scoring='accuracy').mean())
    print(f'[model_build] cross-val accuracy={score:.3f} on {len(X)} rows')
    if score < 0.5:
        print('[model-build] quality gate failed; not publishing', file=sys.stderr)
        sys.exit(4)

    # Footprint safety (plan \u00a719)
    if model_footprint() >= FOOTPRINT_WARN:
        print('[model_build] WARNING: footprint at/above warn threshold', file=sys.stderr)

    os.makedirs(MODEL_DIR, exist_ok=True)

    # Atomic write with backup + compression (plan \u00a724,26)
    tmp_model = os.path.join(MODEL_DIR, 'ai_agent.joblib.tmp')
    final_model = os.path.join(MODEL_DIR, 'ai_agent.joblib')
    joblib.dump({'rf': rf, 'sgd': None}, tmp_model, compress=3)
    if os.path.exists(final_model):
        shutil.copy(final_model, final_model + '.prev')
    os.replace(tmp_model, final_model)

    meta = bump_version(read_metadata())
    meta['event_count'] = len(X)
    meta['cross_val_accuracy'] = round(score, 4)
    meta['built_at'] = int(time.time())
    write_metadata(meta)

    print(f'[model_build] published {meta["model_version"]} -> {final_model}')
    print('[model_build] DONE. CI should git add models/ && commit && push.')


if __name__ == '__main__':
    main()
