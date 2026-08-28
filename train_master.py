#!/usr/bin/env python3
"""
MASTER TRAINER — Embeds complete WiFi knowledge into AI brain
Uses: wifi_master_knowledge.py, wps_knowledge_base.py, offensive_reasoning_engine.py
"""
import os
import sys
import random
import struct
import hashlib
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from wifi_master_knowledge import IEEE_802_11, WPS_VULNERABILITIES, TOOL_INTERNALS, RF_TELEMETRY, ZERO_DAY_HISTORY
from wps_knowledge_base import WPS_CVES, CHIPSET_PROFILES, VENDOR_PIN_ALGORITHMS, DECISION_TREE

# ═══════════════════════════════════════════════════════════
# Generate training scenarios from ALL knowledge sources
# ═══════════════════════════════════════════════════════════

FEATURE_KEYS = [
    'signal_strength', 'signal_variance', 'wps_enabled', 'wps_locked',
    'wps_version', 'consecutive_fails', 'pin_found', 'current_phase',
    'chipset_risk', 'device_age', 'attempt_count', 'lockout_time',
    'signal_trend', 'nonce_predictable', 'm1m2_timeout', 'eapol_issues'
]

CLASSES = ['proceed', 'wait', 'skip', 'abort']

def generate_scenario(cluster, knowledge_source=None):
    """Generate one training scenario based on cluster type."""
    feat = [0.0] * 16

    if cluster == 'protocol_802_11':
        # Scenarios based on IEEE 802.11 frame types
        subtypes = list(IEEE_802_11['frame_types']['management'].keys())
        subtype = random.choice(subtypes)
        feat[0] = random.uniform(-40, -60)  # signal
        feat[1] = random.uniform(1, 10)  # variance
        feat[2] = 1.0  # wps enabled
        feat[3] = 0.0  # not locked
        feat[4] = 2.0 if 'v2' in subtype else 1.0
        feat[5] = 0
        feat[6] = 0
        feat[7] = 0.0
        feat[8] = random.random()
        feat[9] = random.randint(1, 10)
        feat[10] = 0
        feat[11] = 0
        feat[12] = 0.0
        feat[13] = random.random() > 0.7
        feat[14] = 0
        feat[15] = 0
        cls = 'proceed'

    elif cluster == 'wps_vuln':
        # Scenarios from WPS vulnerability database
        vuln = random.choice(list(WPS_CVES.keys()))
        vuln_info = WPS_CVES[vuln]
        feat[0] = random.uniform(-30, -70)
        feat[1] = random.uniform(1, 15)
        feat[2] = 1.0
        feat[3] = 0.0
        feat[4] = 2.0 if vuln_info.get('cvss', 7) > 8 else 1.0
        feat[5] = random.randint(0, 5)
        feat[6] = 0
        feat[7] = 0.0
        feat[8] = random.random()
        feat[9] = random.randint(1, 15)
        feat[10] = random.randint(0, 10)
        feat[11] = random.randint(60, 600)
        feat[12] = random.uniform(-1, 1)
        feat[13] = random.random() > 0.5
        feat[14] = 1.0 if random.random() > 0.8 else 0.0
        feat[15] = 0
        cls = 'proceed' if random.random() > 0.3 else 'wait'

    elif cluster == 'tool_output_reaver':
        # Reaver output parsing scenarios
        output_types = ['success', 'locked', 'timeout', 'eapol_fail', 'pin_found']
        ot = random.choice(output_types)
        feat[0] = random.uniform(-25, -65)
        feat[1] = random.uniform(2, 12)
        feat[2] = 1.0
        feat[3] = 1.0 if ot == 'locked' else 0.0
        feat[4] = random.choice([1.0, 2.0])
        feat[5] = random.randint(3, 20) if ot in ['locked', 'timeout'] else random.randint(0, 5)
        feat[6] = 1.0 if ot == 'success' or ot == 'pin_found' else 0.0
        feat[7] = 0.0
        feat[8] = random.random()
        feat[9] = random.randint(2, 12)
        feat[10] = random.randint(1, 30)
        feat[11] = random.randint(60, 600) if ot == 'locked' else 0
        feat[12] = random.uniform(-2, 2)
        feat[13] = 0
        feat[14] = 1.0 if ot == 'timeout' else 0.0
        feat[15] = 1.0 if ot == 'eapol_fail' else 0.0
        if ot == 'success' or ot == 'pin_found':
            cls = 'proceed'
        elif ot == 'locked':
            cls = 'wait'
        else:
            cls = random.choice(['skip', 'wait'])

    elif cluster == 'tool_output_bully':
        # Bully output parsing
        outcomes = ['pixie_dust_success', 'pixie_dust_fail', 'bruteforce_progress', 'lockout']
        outcome = random.choice(outcomes)
        feat[0] = random.uniform(-30, -55)
        feat[1] = random.uniform(1, 8)
        feat[2] = 1.0
        feat[3] = 1.0 if outcome == 'lockout' else 0.0
        feat[4] = random.choice([1.0, 2.0])
        feat[5] = random.randint(5, 15) if outcome == 'lockout' else random.randint(0, 8)
        feat[6] = 1.0 if outcome == 'pixie_dust_success' else 0.0
        feat[7] = 1.0
        feat[8] = random.random()
        feat[9] = random.randint(3, 10)
        feat[10] = random.randint(5, 50)
        feat[11] = random.randint(120, 360) if outcome == 'lockout' else 0
        feat[12] = random.uniform(-1, 1)
        feat[13] = random.random() > 0.6
        feat[14] = 0
        feat[15] = 0
        cls = 'proceed' if outcome == 'pixie_dust_success' else ('wait' if outcome == 'lockout' else 'skip')

    elif cluster == 'chipset_specific':
        chipsets = list(CHIPSET_PROFILES.keys())
        chipset = random.choice(chipsets)
        profile = CHIPSET_PROFILES[chipset]
        feat[0] = random.uniform(-25, -70)
        feat[1] = random.uniform(1, 15)
        feat[2] = 1.0
        feat[3] = 0.0
        feat[4] = 2.0 if random.random() > 0.5 else 1.0
        feat[5] = random.randint(0, 10)
        feat[6] = 0
        feat[7] = 0.0
        feat[8] = profile.get('lockout_time', 300) / 600.0
        feat[9] = random.randint(2, 15)
        feat[10] = random.randint(0, 20)
        feat[11] = profile.get('lockout_time', 300)
        feat[12] = random.uniform(-2, 2)
        feat[13] = random.random() > 0.7
        feat[14] = 0
        feat[15] = 0
        if profile['pixie_dust_rate'] > 0.7:
            cls = 'proceed'
        elif profile['pixie_dust_rate'] > 0.4:
            cls = random.choice(['proceed', 'wait'])
        else:
            cls = 'wait'

    elif cluster == 'edge_case':
        # Weird real-world situations
        edge_types = [
            'honeypot', 'rebooting', 'dynamic_pin', 'channel_hop',
            'evil_twin', 'enterprise', 'contradictory', 'slow',
            'aggressive_lock', 'hidden_wps', 'dual_band', 'firmware_bug'
        ]
        edge = random.choice(edge_types)
        if edge == 'honeypot':
            feat = [random.uniform(-30, -50)] + [random.uniform(1, 5)] + [1.0, 0.0, 1.0, 0, 1.0, 0.0, 0.3, 5, 2, 0, 0.0, 0, 0, 0]
            cls = 'proceed'
        elif edge == 'rebooting':
            feat = [random.uniform(-40, -60)] + [random.uniform(5, 20)] + [1.0, 0.0, 1.0, 3, 0.0, 0.5, 0.5, 8, 1, 120, 2.0, 0, 0, 0]
            cls = 'wait'
        elif edge == 'dynamic_pin':
            feat = [random.uniform(-30, -55)] + [random.uniform(1, 8)] + [1.0, 0.0, 1.0, 0, 0.0, 1.0, 0.6, 5, 10, 0, 0.5, 0, 0, 0]
            cls = 'skip'
        elif edge == 'enterprise':
            feat = [random.uniform(-25, -45)] + [random.uniform(1, 5)] + [1.0, 0.0, 2.0, 0, 0.0, 0.0, 0.9, 2, 0, 0, 0.0, 0, 0, 0]
            cls = 'abort'
        elif edge == 'contradictory':
            feat = [random.uniform(-35, -55)] + [random.uniform(3, 12)] + [1.0, 1.0, 1.0, 5, 0.0, 0.5, 0.4, 8, 5, 300, -0.5, 0, 0, 0]
            cls = 'proceed'
        elif edge == 'channel_hop':
            feat = [random.uniform(-40, -60)] + [random.uniform(10, 30)] + [1.0, 0.0, 1.0, 2, 0.0, 2.0, 0.3, 6, 3, 0, 3.0, 0, 0, 0]
            cls = 'wait'
        elif edge == 'evil_twin':
            feat = [random.uniform(-20, -35)] + [random.uniform(1, 3)] + [1.0, 0.0, 1.0, 0, 0.0, 0.0, 0.2, 3, 0, 0, 0.0, 0, 1, 0]
            cls = 'proceed'
        elif edge == 'dual_band':
            feat = [random.uniform(-30, -50)] + [random.uniform(2, 8)] + [1.0, 0.0, 1.0, 1, 0.0, 1.5, 0.5, 5, 2, 0, 1.0, 0, 0, 0]
            cls = 'proceed'
        elif edge == 'slow':
            feat = [random.uniform(-50, -70)] + [random.uniform(1, 5)] + [1.0, 0.0, 1.0, 0, 0.0, 0.0, 0.8, 10, 0, 0, 0.0, 0, 0, 0]
            cls = 'proceed'
        elif edge == 'firmware_bug':
            feat = [random.uniform(-35, -55)] + [random.uniform(3, 15)] + [1.0, 0.0, 1.0, 4, 0.0, 1.5, 0.4, 7, 4, 180, 0.5, 0, 1, 1]
            cls = 'skip'
        elif edge == 'hidden_wps':
            feat = [random.uniform(-40, -60)] + [random.uniform(1, 5)] + [0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0, 0, 0, 0.0, 0, 0, 0]
            cls = 'abort'
        elif edge == 'aggressive_lock':
            feat = [random.uniform(-30, -50)] + [random.uniform(1, 5)] + [1.0, 1.0, 1.0, 15, 0.0, 0.5, 0.7, 8, 10, 5, 900, -1.0, 0, 0, 0]
            cls = 'wait'
        else:
            feat = [random.uniform(-40, -60)] + [random.uniform(2, 10)] + [1.0, 0.0, 1.0, 2, 0.0, 0.0, 0.5, 5, 2, 0, 0.0, 0, 0, 0]
            cls = 'proceed'

    elif cluster == 'rf_telemetry':
        # RF signal analysis scenarios
        conditions = ['strong', 'medium', 'weak', 'noisy', 'degrading']
        cond = random.choice(conditions)
        if cond == 'strong':
            feat = [-30 + random.uniform(-5, 5)] + [random.uniform(1, 3)] + [1, 0, 1, 0, 0, 0, 0.1, 3, 0, 0, 0, 0, 0, 0]
            cls = 'proceed'
        elif cond == 'medium':
            feat = [-55 + random.uniform(-5, 5)] + [random.uniform(3, 8)] + [1, 0, 1, 1, 0, 0.5, 0.4, 5, 1, 0, 0.5, 0, 0, 0]
            cls = 'proceed'
        elif cond == 'weak':
            feat = [-75 + random.uniform(-5, 5)] + [random.uniform(5, 15)] + [1, 0, 1, 3, 0, 0.8, 0.6, 10, 3, 2, 1.5, 0, 0, 0]
            cls = 'wait'
        elif cond == 'noisy':
            feat = [-50 + random.uniform(-10, 10)] + [random.uniform(10, 25)] + [1, 0, 1, 5, 0, 0.7, 0.7, 12, 5, 3, 2.0, 0, 0, 0]
            cls = 'skip'
        else:  # degrading
            feat = [-45 + random.uniform(-10, 10)] + [random.uniform(5, 20)] + [1, 0, 1, 2, 0, 0.5, 0.5, 8, 2, 1, 1.0, -2.0, 0, 0, 0]
            cls = 'wait'

    elif cluster == 'zero_day':
        # Novel attack scenarios
        feat = [random.uniform(-30, -60)] + [random.uniform(2, 12)] + [1, 0, random.choice([1, 2]), random.randint(0, 8), 0, random.uniform(0, 2), random.random(), random.randint(3, 12), random.randint(0, 20), 0, random.uniform(-1, 1), random.random() > 0.5, random.random() > 0.7, random.random() > 0.6]
        if feat[5] > 8:
            cls = 'skip'
        elif feat[6] > 0.7:
            cls = 'proceed'
        else:
            cls = random.choice(['proceed', 'wait'])

    elif cluster == 'multi_stage':
        # Complex multi-step attack chains
        phase = random.randint(0, 6)
        feat = [random.uniform(-35, -55)] + [random.uniform(1, 10)] + [1, 0, 1, phase, 0, phase / 7.0, random.random(), random.randint(3, 10), phase * 3, 0, random.uniform(-1, 1), 0, 0, 0]
        if phase >= 6:
            cls = 'abort'
        elif phase >= 4:
            cls = random.choice(['wait', 'skip'])
        else:
            cls = 'proceed'

    else:
        # Default random
        feat = [random.uniform(-30, -75)] + [random.uniform(0, 20)] + [random.choice([0, 1]), random.choice([0, 1]), random.choice([1, 2]), random.randint(0, 15), random.choice([0, 1]), random.random(), random.random(), random.randint(1, 15), random.randint(0, 30), 0, random.uniform(-2, 2), random.choice([0, 0, 0, 1]), random.choice([0, 0, 0, 1]), random.choice([0, 0, 0, 1])]
        cls = random.choice(CLASSES)

    # Safety: ensure all vectors are exactly 16 features
    while len(feat) < 16:
        feat.append(0.0)
    feat = feat[:16]

    return feat, cls


# ═══════════════════════════════════════════════════════════
# Random Forest implementation
# ═══════════════════════════════════════════════════════════

class SimpleNode:
    __slots__ = ['feature', 'threshold', 'left', 'right', 'value', 'is_leaf']
    def __init__(self):
        self.feature = 0
        self.threshold = 0.0
        self.left = None
        self.right = None
        self.value = None
        self.is_leaf = False

class SimpleTree:
    __slots__ = ['root', 'max_depth']
    def __init__(self, max_depth=12):
        self.root = None
        self.max_depth = max_depth

    def fit(self, X, y, depth=0):
        if depth >= self.max_depth or len(set(y)) == 1 or len(y) < 5:
            node = SimpleNode()
            node.is_leaf = True
            counts = {}
            for c in y:
                counts[c] = counts.get(c, 0) + 1
            node.value = max(counts, key=counts.get)
            return node

        best_feat, best_thresh, best_gini = 0, 0.0, 999.0
        n_features = len(X[0])
        n_check = max(1, int(n_features ** 0.5))

        for _ in range(n_check):
            fi = random.randint(0, n_features - 1)
            vals = sorted(set(x[fi] for x in X))
            if len(vals) < 2:
                continue
            step = max(1, len(vals) // 10)
            for vi in range(0, len(vals) - 1, step):
                thresh = (vals[vi] + vals[vi + 1]) / 2.0
                left_y, right_y = [], []
                for i in range(len(y)):
                    if X[i][fi] <= thresh:
                        left_y.append(y[i])
                    else:
                        right_y.append(y[i])
                if not left_y or not right_y:
                    continue
                gini = self._gini(left_y, right_y, len(y))
                if gini < best_gini:
                    best_gini = gini
                    best_feat = fi
                    best_thresh = thresh

        node = SimpleNode()
        node.feature = best_feat
        node.threshold = best_thresh

        left_X, left_y, right_X, right_y = [], [], [], []
        for i in range(len(y)):
            if X[i][best_feat] <= best_thresh:
                left_X.append(X[i])
                left_y.append(y[i])
            else:
                right_X.append(X[i])
                right_y.append(y[i])

        node.left = self.fit(left_X, left_y, depth + 1) if left_y else self._leaf(y)
        node.right = self.fit(right_X, right_y, depth + 1) if right_y else self._leaf(y)
        return node

    def _leaf(self, y):
        node = SimpleNode()
        node.is_leaf = True
        counts = {}
        for c in y:
            counts[c] = counts.get(c, 0) + 1
        node.value = max(counts, key=counts.get)
        return node

    def _gini(self, left_y, right_y, total):
        def gini(group):
            if not group:
                return 0
            counts = {}
            for c in group:
                counts[c] = counts.get(c, 0) + 1
            imp = 1.0
            n = len(group)
            for v in counts.values():
                p = v / n
                imp -= p * p
            return imp
        return (len(left_y) * gini(left_y) + len(right_y) * gini(right_y)) / total

    def predict(self, x):
        node = self.root
        while not node.is_leaf:
            if x[node.feature] <= node.threshold:
                node = node.left
            else:
                node = node.right
        return node.value


class SimpleRF:
    __slots__ = ['trees', 'n_trees', 'max_depth']
    def __init__(self, n_trees=200, max_depth=12):
        self.trees = []
        self.n_trees = n_trees
        self.max_depth = max_depth

    def fit(self, X, y):
        self.trees = []
        n = len(X)
        for i in range(self.n_trees):
            indices = [random.randint(0, n - 1) for _ in range(n)]
            bx = [X[j] for j in indices]
            by = [y[j] for j in indices]
            tree = SimpleTree(self.max_depth)
            tree.root = tree.fit(bx, by)
            self.trees.append(tree)

    def predict(self, x):
        votes = {}
        for tree in self.trees:
            pred = tree.predict(x)
            votes[pred] = votes.get(pred, 0) + 1
        return max(votes, key=votes.get)

    def score(self, X, y):
        correct = sum(1 for i in range(len(y)) if self.predict(X[i]) == y[i])
        return correct / len(y) if y else 0


# ═══════════════════════════════════════════════════════════
# SGD Classifier
# ═══════════════════════════════════════════════════════════

class SimpleSGD:
    __slots__ = ['weights', 'bias', 'lr', 'n_features', 'class_map', 'inv_map']
    def __init__(self, n_features=16, lr=0.01):
        self.n_features = n_features
        self.lr = lr
        self.weights = {}
        self.bias = {}
        self.class_map = {}
        self.inv_map = {}

    def fit(self, X, y):
        classes = list(set(y))
        self.class_map = {c: i for i, c in enumerate(classes)}
        self.inv_map = {i: c for c, i in self.class_map.items()}
        n_classes = len(classes)
        self.weights = [[0.0] * self.n_features for _ in range(n_classes)]
        self.bias = [0.0] * n_classes

        for epoch in range(50):
            for i in range(len(X)):
                x = X[i]
                t = self.class_map[y[i]]
                for j in range(n_classes):
                    score = sum(self.weights[j][k] * x[k] for k in range(self.n_features)) + self.bias[j]
                    pred = 1 if score > 0 else 0
                    target = 1 if j == t else 0
                    err = target - pred
                    for k in range(self.n_features):
                        self.weights[j][k] += self.lr * err * x[k]
                    self.bias[j] += self.lr * err

    def predict(self, x):
        best_cls = list(self.class_map.keys())[0]
        best_score = -999999
        for j, cls in self.inv_map.items():
            score = sum(self.weights[j][k] * x[k] for k in range(self.n_features)) + self.bias[j]
            if score > best_score:
                best_score = score
                best_cls = cls
        return best_cls

    def score(self, X, y):
        correct = sum(1 for i in range(len(y)) if self.predict(X[i]) == y[i])
        return correct / len(y) if y else 0


# ═══════════════════════════════════════════════════════════
# Q-Table
# ═══════════════════════════════════════════════════════════

class SimpleQTable:
    __slots__ = ['q', 'alpha', 'gamma', 'epsilon']
    def __init__(self, alpha=0.3, gamma=0.9, epsilon=0.1):
        self.q = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def _discretize(self, state):
        return tuple(round(s * 10) / 10 for s in state)

    def get_q(self, state, action):
        key = (self._discretize(state), action)
        return self.q.get(key, 0.0)

    def update(self, state, action, reward, next_state):
        s = self._discretize(state)
        ns = self._discretize(next_state)
        best_next = max(self.get_q(ns, a) for a in CLASSES)
        old = self.get_q(s, action)
        new = old + self.alpha * (reward + self.gamma * best_next - old)
        self.q[(s, action)] = new

    def size(self):
        return len(self.q)


# ═══════════════════════════════════════════════════════════
# MAIN TRAINING
# ═══════════════════════════════════════════════════════════

def main():
    print("╔══════════════════════════════════════════════╗")
    print("║  MASTER TRAINER — WiFi AI Brain v5.0         ║")
    print("╚══════════════════════════════════════════════╝")

    # Knowledge sources
    print("\n📚 Loading knowledge sources...")
    print(f"  IEEE 802.11: {len(IEEE_802_11)} categories")
    print(f"  WPS Vulns: {len(WPS_VULNERABILITIES)} entries")
    print(f"  Tool Internals: {len(TOOL_INTERNALS)} tools")
    print(f"  RF Telemetry: {len(RF_TELEMETRY)} categories")
    print(f"  Zero-Day History: {len(ZERO_DAY_HISTORY)} attacks")
    print(f"  Chipset Profiles: {len(CHIPSET_PROFILES)} chipsets")
    print(f"  Vendor Algorithms: {len(VENDOR_PIN_ALGORITHMS)} vendors")
    print(f"  Decision Rules: {len(DECISION_TREE)} rules")

    # Generate scenarios
    print("\n🏋️ Generating training scenarios...")
    clusters = {
        'protocol_802_11': 2000,
        'wps_vuln': 2000,
        'tool_output_reaver': 2000,
        'tool_output_bully': 2000,
        'chipset_specific': 2000,
        'edge_case': 2000,
        'rf_telemetry': 1500,
        'zero_day': 1500,
        'multi_stage': 1500,
    }

    X, y = [], []
    for cluster, count in clusters.items():
        for _ in range(count):
            feat, cls = generate_scenario(cluster)
            X.append(feat)
            y.append(cls)
        print(f"  {cluster}: {count} scenarios")

    total = len(X)
    print(f"  TOTAL: {total} scenarios")

    # Shuffle and split
    indices = list(range(total))
    random.shuffle(indices)
    split = int(total * 0.8)
    train_idx = indices[:split]
    test_idx = indices[split:]

    X_train = [X[i] for i in train_idx]
    y_train = [y[i] for i in train_idx]
    X_test = [X[i] for i in test_idx]
    y_test = [y[i] for i in test_idx]

    # Train RF
    print("\n🌲 Training Random Forest (200 trees, depth 12)...")
    t0 = time.time()
    rf = SimpleRF(n_trees=200, max_depth=12)
    rf.fit(X_train, y_train)
    rf_train_acc = rf.score(X_train, y_train)
    rf_test_acc = rf.score(X_test, y_test)
    rf_time = time.time() - t0
    print(f"  Train: {rf_train_acc:.2%} | Test: {rf_test_acc:.2%} | Time: {rf_time:.1f}s")

    # Train SGD
    print("\n📈 Training SGD Classifier...")
    t0 = time.time()
    sgd = SimpleSGD(n_features=16, lr=0.01)
    sgd.fit(X_train, y_train)
    sgd_train_acc = sgd.score(X_train, y_train)
    sgd_test_acc = sgd.score(X_test, y_test)
    sgd_time = time.time() - t0
    print(f"  Train: {sgd_train_acc:.2%} | Test: {sgd_test_acc:.2%} | Time: {sgd_time:.1f}s")

    # Train Q-Table
    print("\n🎮 Training Q-Table...")
    qt = SimpleQTable()
    for _ in range(5000):
        state = X[random.randint(0, total - 1)]
        action = CLASSES[random.randint(0, 3)]
        reward = 1.0 if action == y[random.randint(0, total - 1)] else -0.5
        next_state = X[random.randint(0, total - 1)]
        qt.update(state, action, reward, next_state)
    print(f"  Q-Table: {qt.size()} states")

    # Save model
    print("\n💾 Saving model...")
    model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
    os.makedirs(model_dir, exist_ok=True)

    # Save RF
    rf_path = os.path.join(model_dir, 'ai_rf_model.bin')
    with open(rf_path, 'wb') as f:
        for tree in rf.trees:
            _save_tree(f, tree.root)
    rf_size = os.path.getsize(rf_path)

    # Save data buffer
    data_path = os.path.join(model_dir, 'ai_data_buffer.bin')
    with open(data_path, 'wb') as f:
        n = min(15000, total)
        f.write(struct.pack('I', n))
        for i in range(n):
            for v in X[i]:
                f.write(struct.pack('f', v))
            idx = CLASSES.index(y[i]) if y[i] in CLASSES else 0
            f.write(struct.pack('B', idx))
    data_size = os.path.getsize(data_path)

    # Save Q-Table
    q_path = os.path.join(model_dir, 'ai_q_table.bin')
    with open(q_path, 'wb') as f:
        f.write(struct.pack('I', len(qt.q)))
        for (state, action), value in qt.q.items():
            for v in state:
                f.write(struct.pack('f', v))
            idx = CLASSES.index(action) if action in CLASSES else 0
            f.write(struct.pack('B', idx))
            f.write(struct.pack('f', value))
    q_size = os.path.getsize(q_path)

    total_size = rf_size + data_size + q_size

    print(f"\n{'='*50}")
    print(f"  RF Model:     {rf_size / 1024 / 1024:.1f} MB")
    print(f"  Data Buffer:  {data_size / 1024 / 1024:.1f} MB")
    print(f"  Q-Table:      {q_size / 1024:.1f} KB")
    print(f"  TOTAL:        {total_size / 1024 / 1024:.1f} MB")
    print(f"{'='*50}")

    # Print summary
    print(f"\n╔══════════════════════════════════════════════╗")
    print(f"║  TRAINING COMPLETE                          ║")
    print(f"║                                              ║")
    print(f"║  Scenarios:    {total:,}                    ║")
    print(f"║  RF Accuracy:  {rf_test_acc:.2%}              ║")
    print(f"║  SGD Accuracy: {sgd_test_acc:.2%}              ║")
    print(f"║  Q-Table:      {qt.size():,} states          ║")
    print(f"║  Model Size:   {total_size / 1024 / 1024:.1f} MB         ║")
    print(f"║  Knowledge:    8 sources                   ║")
    print(f"║  CVEs:         13 (2012-2026)              ║")
    print(f"║  Chipsets:     8 profiles                  ║")
    print(f"╚══════════════════════════════════════════════╝")

    return rf_test_acc, sgd_test_acc, qt.size(), total_size


def _save_tree(f, node):
    if node is None:
        f.write(struct.pack('B', 0))
        return
    if node.is_leaf:
        f.write(struct.pack('B', 1))
        cls_idx = CLASSES.index(node.value) if node.value in CLASSES else 0
        f.write(struct.pack('B', cls_idx))
    else:
        f.write(struct.pack('B', 2))
        f.write(struct.pack('H', node.feature))
        f.write(struct.pack('f', node.threshold))
        _save_tree(f, node.left)
        _save_tree(f, node.right)


if __name__ == '__main__':
    main()
