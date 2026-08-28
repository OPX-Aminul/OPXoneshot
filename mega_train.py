#!/usr/bin/env python3
"""MEGA TRAINING — Maximum benchmark level AI brain."""
import os, json, random, pickle
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold

random.seed(42); np.random.seed(42)
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
os.makedirs(D, exist_ok=True)
A = ('proceed', 'wait', 'skip', 'abort')

def norm(d):
    return max(0.0, min(1.0, (d + 90) / 50))

def mf(s, v, lk, vu, at, td, dl, mm, fl, hk=0, ci=0, cc=0.0, ns=-90.0):
    so = 1.0 if s > -70 else 0.0
    fr = td / (td + mm) if (td + mm) > 0 else 0.0
    nn = (max(-100, min(0, ns)) + 100) / 100
    return [norm(s), 1.0 if v == '2.0' else 0.0, int(lk), int(vu),
            min(at, 20) / 20, min(td, 10) / 10, min(dl, 30) / 30,
            min(mm, 8) / 8, min(fl, 10) / 10, so, 0.5, fr,
            min(hk, 10) / 10, min(ci, 7) / 7, cc, nn]

S = []

# Easy targets (strong signal, vulnerable, no lock)
for _ in range(2000):
    s = random.uniform(-35, -55)
    S.append((mf(s, '1.0', False, True, random.randint(1, 3), 0,
             random.uniform(0.5, 2), random.randint(2, 5), 0), 'proceed'))

# Medium targets (decent signal, some issues)
for _ in range(2000):
    s = random.uniform(-50, -70)
    lk = random.random() < 0.3
    td = random.randint(0, 3)
    S.append((mf(s, '1.0', lk, True, random.randint(1, 5), td,
             random.uniform(1, 5), random.randint(0, 3), random.randint(0, 2)),
             'wait' if lk else 'proceed'))

# Hard targets (weak signal, many failures)
for _ in range(1500):
    s = random.uniform(-70, -85)
    td = random.randint(2, 8)
    fl = random.randint(3, 8)
    S.append((mf(s, '1.0', random.random() < 0.6, False, random.randint(3, 10), td,
             random.uniform(3, 15), random.randint(0, 2), fl),
             'skip' if fl > 5 else 'wait'))

# Dead targets (no response)
for _ in range(1000):
    S.append((mf(random.uniform(-75, -90), '1.0', True, False,
             random.randint(5, 20), random.randint(5, 10), random.uniform(10, 30),
             0, random.randint(6, 10)), 'abort'))

# WPS v2 targets
for _ in range(1000):
    s = random.uniform(-40, -75)
    S.append((mf(s, '2.0', random.random() < 0.5, random.random() < 0.3,
             random.randint(1, 8), random.randint(0, 5), random.uniform(1, 8),
             random.randint(0, 4), random.randint(0, 5)),
             'proceed' if s > -60 and random.random() < 0.6 else 'wait'))

# Different chipsets
for ci in range(8):
    for _ in range(500):
        s = random.uniform(-35, -85)
        S.append((mf(s, random.choice(['1.0', '2.0']), random.random() < 0.4,
                 random.random() < 0.5, random.randint(1, 12), random.randint(0, 6),
                 random.uniform(0.5, 12), random.randint(0, 5), random.randint(0, 6),
                 0, ci, random.uniform(0, 0.8), random.uniform(-95, -55)),
                 random.choice(A)))

# Attack phase specific
for _ in range(1500):
    ph = random.choice([0, 1, 2])
    s = random.uniform(-30, -80)
    att = ph + 1
    td = random.randint(0, 5) if ph > 0 else 0
    fl = random.randint(0, 4) if ph > 1 else 0
    lb = 'proceed' if s > -65 and td < 3 and fl < 3 else \
         'wait' if td < 4 else 'skip' if fl > 3 else 'abort'
    S.append((mf(s, '1.0', random.random() < 0.3, random.random() < 0.6, att, td,
             random.uniform(1, 8), random.randint(0, 4), fl, random.randint(0, 3),
             random.randint(0, 7), random.uniform(0, 0.5), random.uniform(-80, -60)), lb))

# Edge cases
for _ in range(1000):
    S.append((mf(-25, '1.0', True, True, 1, 0, 0.1, 5, 0, 0, 1, 0.0, -40), 'wait'))
    S.append((mf(-89, '1.0', False, False, 1, 0, 0.5, 0, 0, 0, 0, 0.9, -95), 'skip'))
    S.append((mf(-30, '1.0', False, True, 1, 0, 0.1, 4, 0, 0, 1, 0.0, -50), 'proceed'))
    S.append((mf(-90, '2.0', True, False, 20, 10, 30, 0, 10, 10, 7, 1.0, -100), 'abort'))

random.shuffle(S)
X = np.array([s[0] for s in S])
y = np.array([s[1] for s in S])
print(f"Scenarios: {len(S):,}")
print(f"Classes: {dict(zip(*np.unique(y, return_counts=True)))}")

# RF
print("Training RF (200 trees)...", flush=True)
rf = RandomForestClassifier(n_estimators=200, max_depth=15, min_samples_leaf=2,
                            random_state=42, n_jobs=-1, class_weight='balanced')
rf.fit(X, y)
cv = cross_val_score(rf, X, y, cv=StratifiedKFold(5, shuffle=True, random_state=42), n_jobs=-1)
print(f"  RF CV: {cv.mean():.4f} +/- {cv.std():.4f}")

# SGD
print("Training SGD...", flush=True)
sgd = SGDClassifier(loss='log_loss', random_state=42, learning_rate='optimal', eta0=0.001)
sgd.fit(X, y)
cv2 = cross_val_score(sgd, X, y, cv=StratifiedKFold(5, shuffle=True, random_state=42), n_jobs=-1)
print(f"  SGD CV: {cv2.mean():.4f}")

# Q-Table
print("Training Q-Table (5000 episodes)...", flush=True)
qt = {}
for ep in range(5000):
    idx = random.randint(0, len(S) - 1)
    feat, label = S[idx]
    s_key = f"{feat[0]:.1f}_{'L' if feat[2] > 0.5 else 'N'}_{int(feat[8]*10)}"
    if s_key not in qt:
        qt[s_key] = {a: 0.0 for a in A}
    r = 1.0 if label == 'proceed' else (0.3 if label == 'wait' else -0.5)
    act = random.choice(A)
    qt[s_key][act] += 0.1 * (r + 0.95 * max(qt[s_key].values()) - qt[s_key][act])
print(f"  Q-Table: {len(qt):,} states")

# Save
joblib.dump({'rf': rf, 'sgd': sgd}, os.path.join(D, 'ai_agent.joblib'), compress=3)
with open(os.path.join(D, 'ai_data.pkl'), 'wb') as f:
    pickle.dump({'X': [s[0] for s in S[-5000:]], 'y': [s[1] for s in S[-5000:]],
                 'rewards': [0.5] * 5000}, f)
with open(os.path.join(D, 'ai_qtable.pkl'), 'wb') as f:
    pickle.dump(qt, f)

meta = {
    'version': 'v5.0.0', 'model_version': 'v5.0.0-mega',
    'event_count': len(S),
    'cv_accuracy_rf': round(cv.mean(), 4),
    'cv_accuracy_sgd': round(cv2.mean(), 4),
    'q_table_states': len(qt),
    'feature_names': ['signal', 'wps_ver', 'wps_locked', 'is_vuln', 'attempt',
                      'timeouts', 'resp_delay', 'm_msgs', 'fails', 'sig_ok',
                      'oui', 'frame_loss', 'hist_locks', 'chip_id',
                      'channel_congestion', 'noise_floor'],
    'training_scenarios': len(S),
    'rf_trees': 200, 'rf_depth': 15,
    'advancements': ['chipset_fingerprinting', 'mab_delay', 'dqn_neural',
                     'stealth_jitter', 'poison_guard', 'swarm_mode',
                     'cognitive_reasoning', 'cve_parser', 'resilience_manager',
                     'mathematical_reasoning', 'code_intelligence',
                     'error_interpreter', 'adaptive_evasion',
                     'zero_day_hunter', 'dynamic_pacing',
                     'autonomous_exploit_generator']
}
with open(os.path.join(D, 'model_metadata.json'), 'w') as f:
    json.dump(meta, f, indent=2, default=str)

sz = os.path.getsize(os.path.join(D, 'ai_agent.joblib'))
print(f"\n{'='*50}")
print(f"MEGA TRAINING COMPLETE!")
print(f"Scenarios: {len(S):,}")
print(f"RF: {cv.mean():.4f} | SGD: {cv2.mean():.4f}")
print(f"Q-Table: {len(qt):,} states")
print(f"Model: {sz/1024/1024:.1f} MB")
print(f"{'='*50}")
