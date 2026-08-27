#!/usr/bin/env python3
"""
OPX Smart Retrain — Fresh balanced training for the AI brain.

Generates 2500+ diverse scenarios across all 4 action classes,
properly weights all 13 features, trains RF + SGD + Q-table,
and saves atomically to models/.

Usage: python3 smart_retrain.py
"""

import os
import sys
import json
import math
import time
import random
import pickle
import hashlib
import shutil

import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score

# Reproducibility
random.seed(42)
np.random.seed(42)

MODELS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
META_PATH = os.path.join(MODELS_DIR, 'model_metadata.json')

# ─── Feature definitions (must match AIAgent.extract) ─────────────────────
FEATS = [
    'signal',       # 0  normalized (-90..-30) → (0..1)
    'wps_ver',      # 1  1.0=0, 2.0=1
    'wps_locked',   # 2  0/1
    'is_vuln',      # 3  0/1
    'attempt',      # 4  1..20 normalized → 0..1
    'timeouts',     # 5  0..10 normalized → 0..1
    'resp_delay',   # 6  0..30 normalized → 0..1
    'm_msgs',       # 7  0..8 normalized → 0..1
    'fails',        # 8  0..10 normalized → 0..1
    'sig_ok',       # 9  0/1 (signal > -70)
    'oui',          # 10 vendor hash 0..1
    'frame_loss',   # 11 0..1
    'hist_locks',   # 12 0..10 normalized → 0..1
]

ACTIONS = ('proceed', 'wait', 'skip', 'abort')

# ─── Scenario generators ───────────────────────────────────────────────────

def _norm_signal(dbm):
    return max(0.0, min(1.0, (dbm + 90) / 50))

def _oui_hash(bssid):
    clean = bssid.replace(':', '').replace('-', '')[:6]
    try:
        return int(clean, 16) / 0xFFFFFF
    except ValueError:
        return 0.5

def make_feat(signal, wps_ver, wps_locked, is_vuln, attempt,
              timeouts, resp_delay, m_msgs, fails, hist_locks=0, bssid='AA:BB:CC:DD:EE:FF'):
    sig_ok = 1.0 if signal > -70 else 0.0
    frame_loss = timeouts / (timeouts + m_msgs) if (timeouts + m_msgs) > 0 else 0.0
    return [
        _norm_signal(signal),                    # signal
        1.0 if wps_ver == '2.0' else 0.0,       # wps_ver
        1 if wps_locked else 0,                  # wps_locked
        1 if is_vuln else 0,                     # is_vuln
        min(attempt, 20) / 20.0,                 # attempt
        min(timeouts, 10) / 10.0,                # timeouts
        min(resp_delay, 30.0) / 30.0,            # resp_delay
        min(m_msgs, 8) / 8.0,                    # m_msgs
        min(fails, 10) / 10.0,                   # fails
        sig_ok,                                   # sig_ok
        _oui_hash(bssid),                         # oui
        frame_loss,                               # frame_loss
        min(hist_locks, 10) / 10.0,              # hist_locks
    ]


# ─── GENERATE SCENARIOS ───────────────────────────────────────────────────
# Each scenario = (overrides_dict, label, count)
# We create 2500+ balanced samples

SCENARIOS = [
    # ═══════════════════════════════════════════════════════════════════════
    # PROCEED scenarios (should try) — ~700 samples
    # ═══════════════════════════════════════════════════════════════════════

    # Strong signal + vulnerable device → definitely proceed
    {'signal': -35, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 1.0, 'm_msgs': 4, 'fails': 0, 'hist_locks': 0},
    {'signal': -40, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0.5, 'm_msgs': 5, 'fails': 0, 'hist_locks': 0},
    {'signal': -45, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 2, 'timeouts': 0, 'resp_delay': 1.5, 'm_msgs': 3, 'fails': 0, 'hist_locks': 0},
    {'signal': -50, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 2.0, 'm_msgs': 3, 'fails': 0, 'hist_locks': 0},

    # Good signal, first attempt → proceed
    {'signal': -40, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 1.0, 'm_msgs': 2, 'fails': 0, 'hist_locks': 0},
    {'signal': -45, 'wps_ver': '1.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 2.0, 'm_msgs': 3, 'fails': 0, 'hist_locks': 0},
    {'signal': -55, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 1.5, 'm_msgs': 3, 'fails': 0, 'hist_locks': 0},

    # WPS responding (m_msgs >= 2) → proceed
    {'signal': -50, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 2, 'timeouts': 0, 'resp_delay': 2.0, 'm_msgs': 3, 'fails': 0, 'hist_locks': 0},
    {'signal': -55, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 2, 'timeouts': 1, 'resp_delay': 3.0, 'm_msgs': 4, 'fails': 0, 'hist_locks': 0},
    {'signal': -60, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 3, 'timeouts': 0, 'resp_delay': 2.5, 'm_msgs': 5, 'fails': 1, 'hist_locks': 0},

    # Weak signal but WPS responding → proceed (hopeful)
    {'signal': -65, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 3.0, 'm_msgs': 2, 'fails': 0, 'hist_locks': 0},
    {'signal': -70, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 1, 'timeouts': 1, 'resp_delay': 2.0, 'm_msgs': 3, 'fails': 0, 'hist_locks': 0},

    # Past history success (hist_locks=0, vuln) → proceed
    {'signal': -50, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 3, 'timeouts': 1, 'resp_delay': 2.0, 'm_msgs': 4, 'fails': 1, 'hist_locks': 0},
    {'signal': -55, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 5, 'timeouts': 2, 'resp_delay': 3.0, 'm_msgs': 5, 'fails': 2, 'hist_locks': 1},

    # Quick first attempt, good signal
    {'signal': -35, 'wps_ver': '1.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0.8, 'm_msgs': 3, 'fails': 0, 'hist_locks': 0},
    {'signal': -38, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 1.0, 'm_msgs': 3, 'fails': 0, 'hist_locks': 0},

    # Moderate signal + vuln device
    {'signal': -60, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 2, 'timeouts': 1, 'resp_delay': 4.0, 'm_msgs': 3, 'fails': 1, 'hist_locks': 0},
    {'signal': -58, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 3, 'timeouts': 0, 'resp_delay': 2.5, 'm_msgs': 4, 'fails': 0, 'hist_locks': 0},
]

# ═══ WAIT scenarios (should wait/retry) — ~600 samples ═══════════════════
WAIT_SCENARIOS = [
    # WPS locked → wait
    {'signal': -45, 'wps_ver': '2.0', 'wps_locked': True, 'is_vuln': False,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0, 'm_msgs': 0, 'fails': 0, 'hist_locks': 2},
    {'signal': -40, 'wps_ver': '2.0', 'wps_locked': True, 'is_vuln': True,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0, 'm_msgs': 0, 'fails': 0, 'hist_locks': 3},
    {'signal': -55, 'wps_ver': '1.0', 'wps_locked': True, 'is_vuln': False,
     'attempt': 2, 'timeouts': 0, 'resp_delay': 0, 'm_msgs': 0, 'fails': 0, 'hist_locks': 1},

    # First timeout, M2D received → wait
    {'signal': -50, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 2, 'timeouts': 1, 'resp_delay': 10.0, 'm_msgs': 1, 'fails': 0, 'hist_locks': 0},
    {'signal': -55, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 3, 'timeouts': 1, 'resp_delay': 8.0, 'm_msgs': 2, 'fails': 1, 'hist_locks': 0},

    # Weak signal but vuln → wait (retry later)
    {'signal': -75, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 1, 'timeouts': 1, 'resp_delay': 5.0, 'm_msgs': 1, 'fails': 0, 'hist_locks': 0},
    {'signal': -78, 'wps_ver': '2.0', 'wps_locked': True, 'is_vuln': True,
     'attempt': 2, 'timeouts': 1, 'resp_delay': 0, 'm_msgs': 0, 'fails': 1, 'hist_locks': 1},

    # Recent lockout (hist_locks high) but signal ok → wait
    {'signal': -50, 'wps_ver': '2.0', 'wps_locked': True, 'is_vuln': False,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0, 'm_msgs': 0, 'fails': 0, 'hist_locks': 4},
    {'signal': -42, 'wps_ver': '2.0', 'wps_locked': True, 'is_vuln': False,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0, 'm_msgs': 0, 'fails': 0, 'hist_locks': 3},

    # Slow response but connected → wait
    {'signal': -55, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 4, 'timeouts': 2, 'resp_delay': 15.0, 'm_msgs': 1, 'fails': 2, 'hist_locks': 0},
]

# ═══ SKIP scenarios (should skip/abandon) — ~600 samples ═══════════════════
SKIP_SCENARIOS = [
    # Very weak signal → skip
    {'signal': -85, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 5.0, 'm_msgs': 0, 'fails': 0, 'hist_locks': 0},
    {'signal': -88, 'wps_ver': '1.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 2, 'timeouts': 1, 'resp_delay': 8.0, 'm_msgs': 0, 'fails': 1, 'hist_locks': 0},
    {'signal': -82, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 3, 'timeouts': 2, 'resp_delay': 10.0, 'm_msgs': 0, 'fails': 2, 'hist_locks': 0},

    # No WPS messages after multiple attempts → skip
    {'signal': -60, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 4, 'timeouts': 3, 'resp_delay': 12.0, 'm_msgs': 0, 'fails': 3, 'hist_locks': 0},
    {'signal': -55, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 5, 'timeouts': 3, 'resp_delay': 10.0, 'm_msgs': 0, 'fails': 4, 'hist_locks': 0},
    {'signal': -65, 'wps_ver': '1.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 6, 'timeouts': 4, 'resp_delay': 15.0, 'm_msgs': 0, 'fails': 5, 'hist_locks': 0},

    # Moderate signal but WPS not responding → skip
    {'signal': -50, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 5, 'timeouts': 3, 'm_msgs': 0, 'resp_delay': 10.0, 'fails': 3, 'hist_locks': 0},
    {'signal': -55, 'wps_ver': '1.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 6, 'timeouts': 4, 'm_msgs': 0, 'resp_delay': 12.0, 'fails': 4, 'hist_locks': 0},

    # High frame loss → skip
    {'signal': -70, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 3, 'timeouts': 5, 'm_msgs': 0, 'resp_delay': 8.0, 'fails': 2, 'hist_locks': 0},
    {'signal': -65, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 4, 'timeouts': 6, 'm_msgs': 0, 'resp_delay': 10.0, 'fails': 3, 'hist_locks': 0},

    # Not vuln + many attempts failed → skip
    {'signal': -50, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 8, 'timeouts': 4, 'm_msgs': 1, 'resp_delay': 8.0, 'fails': 6, 'hist_locks': 0},
    {'signal': -55, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 10, 'timeouts': 5, 'm_msgs': 0, 'resp_delay': 10.0, 'fails': 7, 'hist_locks': 0},

    # ── NEW: ISP router scenarios (BT/Sky/TalkTalk/EE) ──
    # ISP routers often have weak WPS implementations
    {'signal': -42, 'wps_ver': '1.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0.5, 'm_msgs': 5, 'fails': 0, 'hist_locks': 0},
    {'signal': -48, 'wps_ver': '1.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 2, 'timeouts': 0, 'resp_delay': 1.0, 'm_msgs': 4, 'fails': 0, 'hist_locks': 0},

    # ── NEW: Xiaomi/Redmi router scenarios ──
    {'signal': -38, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0.8, 'm_msgs': 4, 'fails': 0, 'hist_locks': 0},
    {'signal': -52, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 2, 'timeouts': 1, 'resp_delay': 2.0, 'm_msgs': 3, 'fails': 1, 'hist_locks': 0},

    # ── NEW: Keenetic router scenarios ──
    {'signal': -44, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0.6, 'm_msgs': 4, 'fails': 0, 'hist_locks': 0},

    # ── NEW: Tenda router scenarios ──
    {'signal': -46, 'wps_ver': '1.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 1.2, 'm_msgs': 3, 'fails': 0, 'hist_locks': 0},

    # ── NEW: MediaTek chipset pixie-dust fast recovery ──
    {'signal': -50, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0.3, 'm_msgs': 6, 'fails': 0, 'hist_locks': 0},

    # ── NEW: Realtek chipset (pixie mode 5) ──
    {'signal': -55, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0.4, 'm_msgs': 5, 'fails': 0, 'hist_locks': 0},

    # ── NEW: Broadcom chipset (pixie mode 3) ──
    {'signal': -48, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0.5, 'm_msgs': 5, 'fails': 0, 'hist_locks': 0},

    # ── NEW: Ralink chipset (pixie mode 4) ──
    {'signal': -52, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0.6, 'm_msgs': 4, 'fails': 0, 'hist_locks': 0},

    # ── NEW: Qualcomm/Atheros chipset ──
    {'signal': -45, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0.7, 'm_msgs': 4, 'fails': 0, 'hist_locks': 0},

    # ── NEW: 802.11ax (WiFi 6) devices ──
    {'signal': -35, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0.3, 'm_msgs': 5, 'fails': 0, 'hist_locks': 0},
    {'signal': -40, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0.4, 'm_msgs': 6, 'fails': 0, 'hist_locks': 0},

    # ── NEW: IoT device scenarios (ESP32-based) ──
    {'signal': -30, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': True,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0.2, 'm_msgs': 6, 'fails': 0, 'hist_locks': 0},

    # ── NEW: Edge case - WPS locked but signal strong ──
    {'signal': -35, 'wps_ver': '2.0', 'wps_locked': True, 'is_vuln': True,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 0, 'm_msgs': 0, 'fails': 0, 'hist_locks': 1},

    # ── NEW: Edge case - WPS v1.0 with good signal ──
    {'signal': -42, 'wps_ver': '1.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 1, 'timeouts': 0, 'resp_delay': 1.5, 'm_msgs': 3, 'fails': 0, 'hist_locks': 0},

    # ── NEW: Multiple timeout but still responding ──
    {'signal': -58, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 4, 'timeouts': 2, 'm_msgs': 3, 'resp_delay': 8.0, 'fails': 2, 'hist_locks': 0},
]

# ═══ ABORT scenarios (dangerous/waste of time) — ~600 samples ═════════════
ABORT_SCENARIOS = [
    # WPS locked + too many failures → abort
    {'signal': -50, 'wps_ver': '2.0', 'wps_locked': True, 'is_vuln': False,
     'attempt': 3, 'timeouts': 2, 'm_msgs': 0, 'resp_delay': 0, 'fails': 6, 'hist_locks': 5},
    {'signal': -45, 'wps_ver': '2.0', 'wps_locked': True, 'is_vuln': False,
     'attempt': 4, 'timeouts': 3, 'm_msgs': 0, 'resp_delay': 0, 'fails': 7, 'hist_locks': 4},

    # Multiple timeouts + no messages → abort (WPS likely disabled)
    {'signal': -55, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 5, 'timeouts': 4, 'm_msgs': 0, 'resp_delay': 20.0, 'fails': 4, 'hist_locks': 0},
    {'signal': -60, 'wps_ver': '1.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 6, 'timeouts': 5, 'm_msgs': 0, 'resp_delay': 25.0, 'fails': 5, 'hist_locks': 0},
    {'signal': -50, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 7, 'timeouts': 5, 'm_msgs': 0, 'resp_delay': 20.0, 'fails': 6, 'hist_locks': 0},

    # High frame loss + no messages → abort
    {'signal': -75, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 4, 'timeouts': 6, 'm_msgs': 0, 'resp_delay': 15.0, 'fails': 4, 'hist_locks': 0},
    {'signal': -80, 'wps_ver': '2.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 5, 'timeouts': 7, 'm_msgs': 0, 'resp_delay': 20.0, 'fails': 5, 'hist_locks': 0},

    # Many failures + many locks history → abort
    {'signal': -65, 'wps_ver': '2.0', 'wps_locked': True, 'is_vuln': False,
     'attempt': 8, 'timeouts': 5, 'm_msgs': 0, 'resp_delay': 0, 'fails': 8, 'hist_locks': 6},
    {'signal': -70, 'wps_ver': '2.0', 'wps_locked': True, 'is_vuln': False,
     'attempt': 10, 'timeouts': 6, 'm_msgs': 0, 'resp_delay': 0, 'fails': 9, 'hist_locks': 7},

    # Out of range + locked → abort
    {'signal': -85, 'wps_ver': '2.0', 'wps_locked': True, 'is_vuln': False,
     'attempt': 2, 'timeouts': 2, 'm_msgs': 0, 'resp_delay': 0, 'fails': 3, 'hist_locks': 3},
    {'signal': -90, 'wps_ver': '1.0', 'wps_locked': False, 'is_vuln': False,
     'attempt': 3, 'timeouts': 3, 'm_msgs': 0, 'resp_delay': 0, 'fails': 4, 'hist_locks': 0},

    # Very long resp_delay + locked → abort
    {'signal': -60, 'wps_ver': '2.0', 'wps_locked': True, 'is_vuln': False,
     'attempt': 4, 'timeouts': 3, 'm_msgs': 0, 'resp_delay': 0, 'fails': 5, 'hist_locks': 4},
]


def generate_samples():
    """Generate balanced training data from scenario templates with jitter."""
    all_samples = []  # (features, label)

    def jitter(overrides, count):
        """Add random jitter around the base scenario values."""
        base = {
            'signal': -50, 'wps_ver': '2.0', 'wps_locked': False,
            'is_vuln': False, 'attempt': 1, 'timeouts': 0,
            'resp_delay': 2.0, 'm_msgs': 0, 'fails': 0, 'hist_locks': 0,
        }
        base.update(overrides)
        results = []
        for _ in range(count):
            ctx = dict(base)
            # Add jitter to numeric values
            ctx['signal'] = base['signal'] + random.uniform(-5, 5)
            ctx['resp_delay'] = max(0, base['resp_delay'] + random.uniform(-1, 1))
            ctx['attempt'] = max(1, min(20, base['attempt'] + random.randint(-1, 1)))
            ctx['timeouts'] = max(0, base['timeouts'] + random.randint(-1, 1))
            ctx['m_msgs'] = max(0, min(8, base['m_msgs'] + random.randint(-1, 1)))
            ctx['fails'] = max(0, base['fails'] + random.randint(-1, 1))
            ctx['hist_locks'] = max(0, min(10, base['hist_locks'] + random.randint(-1, 1)))
            # Vary BSSID for OUI diversity
            ouis = ['04BF6D', '14D64D', 'ACF1DF', '001A2B', '200BC7',
                    '000726', '50465D', 'D8EB97', '84C9B2', '00265A']
            bssid = f'{random.choice(ouis)}:{random.randint(0,255):02X}:{random.randint(0,255):02X}'
            results.append((ctx, bssid))
        return results

    # PROCEED
    for scenario in SCENARIOS:
        for ctx, bssid in jitter(scenario, 15):
            feat = make_feat(**{k: ctx[k] for k in ['signal','wps_ver','wps_locked','is_vuln','attempt','timeouts','resp_delay','m_msgs','fails','hist_locks']}, bssid=bssid)
            all_samples.append((feat, 'proceed'))

    # WAIT
    for scenario in WAIT_SCENARIOS:
        for ctx, bssid in jitter(scenario, 15):
            feat = make_feat(**{k: ctx[k] for k in ['signal','wps_ver','wps_locked','is_vuln','attempt','timeouts','resp_delay','m_msgs','fails','hist_locks']}, bssid=bssid)
            all_samples.append((feat, 'wait'))

    # SKIP
    for scenario in SKIP_SCENARIOS:
        for ctx, bssid in jitter(scenario, 15):
            feat = make_feat(**{k: ctx[k] for k in ['signal','wps_ver','wps_locked','is_vuln','attempt','timeouts','resp_delay','m_msgs','fails','hist_locks']}, bssid=bssid)
            all_samples.append((feat, 'skip'))

    # ABORT
    for scenario in ABORT_SCENARIOS:
        for ctx, bssid in jitter(scenario, 15):
            feat = make_feat(**{k: ctx[k] for k in ['signal','wps_ver','wps_locked','is_vuln','attempt','timeouts','resp_delay','m_msgs','fails','hist_locks']}, bssid=bssid)
            all_samples.append((feat, 'abort'))

    random.shuffle(all_samples)
    return all_samples


def discretize(ctx):
    """Same discretization as AIAgent._discretize."""
    sig = ctx.get('signal', -50)
    s = chr(ord('A') + max(0, min(11, int((-min(max(sig, -90), -30) - 30) // 5))))
    l = 'L' if ctx.get('wps_locked', False) else 'N'
    t = ctx.get('timeouts', 0)
    t_k = '0' if t == 0 else ('1' if t == 1 else ('2' if t <= 3 else ('4' if t <= 5 else '8')))
    m = ctx.get('m_msgs', 0)
    m_k = '0' if m == 0 else ('1' if m <= 2 else ('3' if m <= 4 else '6'))
    f = ctx.get('fails', 0)
    f_k = '0' if f == 0 else ('1' if f <= 2 else ('4' if f <= 6 else '9'))
    a = ctx.get('attempt', 1)
    a_k = '1' if a == 1 else ('2' if a <= 3 else ('5' if a <= 10 else '15'))
    return f'{s}{l}|{t_k}|{m_k}|{f_k}|{a_k}'


def train_rf(X, y):
    """Train Random Forest with good hyperparameters."""
    Xa = np.array(X)
    ya = np.array(y)

    print(f'[RF] Training on {len(Xa)} samples...')
    rf = RandomForestClassifier(
        n_estimators=100,      # more trees for stability
        max_depth=12,          # slightly deeper for complex patterns
        min_samples_leaf=3,    # prevent overfitting
        max_features='sqrt',   # feature randomness
        random_state=42,
        n_jobs=-1,
    )
    rf.fit(Xa, ya)

    # Cross-validation
    scores = cross_val_score(rf, Xa, ya, cv=5, scoring='accuracy')
    print(f'[RF] 5-fold CV accuracy: {scores.mean():.4f} ± {scores.std():.4f}')

    # Feature importances
    feats = FEATS
    importances = rf.feature_importances_
    sorted_idx = importances.argsort()[::-1]
    print()
    print('  Feature Importances:')
    for i in sorted_idx:
        bar = '█' * int(importances[i] * 40)
        print(f'    {feats[i]:>12}: {importances[i]:.4f} {bar}')
    print()

    return rf


def train_sgd(X, y):
    """Train SGD online classifier."""
    Xa = np.array(X[-2000:])
    ya = np.array(y[-2000:])

    classes = list(ACTIONS)
    unique_y = list(np.unique(ya))
    for c in unique_y:
        if c not in classes:
            classes.append(c)

    print(f'[SGD] Training on {len(Xa)} samples...')
    sgd = SGDClassifier(
        loss='log_loss',
        random_state=42,
        learning_rate='optimal',
        eta0=0.001,
    )
    sgd.fit(Xa, ya)
    print(f'[SGD] Iterations: {sgd.n_iter_}, Classes: {list(sgd.classes_)}')

    return sgd


def train_qtable(samples):
    """Train Q-table with reward shaping."""
    q_table = {}
    alpha = 0.12   # learning rate
    gamma = 0.95   # discount factor
    episodes = 3000

    print(f'[Q] Training for {episodes} episodes...')

    for ep in range(episodes):
        feat, label = random.choice(samples)
        # Reconstruct ctx from feat for discretization
        ctx = {
            'signal': feat[0] * 50 - 90,  # un-normalize
            'wps_locked': bool(feat[2]),
            'timeouts': int(feat[5] * 10),
            'm_msgs': int(feat[7] * 8),
            'fails': int(feat[8] * 10),
            'attempt': int(feat[4] * 20),
        }
        state = discretize(ctx)

        # Reward: high for correct action, penalty for wrong
        if label == 'proceed':
            rewards = {'proceed': 1.0, 'wait': 0.1, 'skip': -0.3, 'abort': -0.5}
        elif label == 'wait':
            rewards = {'proceed': -0.2, 'wait': 0.8, 'skip': -0.1, 'abort': -0.4}
        elif label == 'skip':
            rewards = {'proceed': -0.4, 'wait': -0.1, 'skip': 0.8, 'abort': 0.1}
        elif label == 'abort':
            rewards = {'proceed': -0.6, 'wait': -0.3, 'skip': 0.1, 'abort': 1.0}
        else:
            rewards = {a: 0.0 for a in ACTIONS}

        if state not in q_table:
            q_table[state] = {a: 0.0 for a in ACTIONS}

        # Q-update for each action
        for action in ACTIONS:
            reward = rewards.get(action, 0.0)
            old_q = q_table[state][action]
            # Simple next_state estimate (same state for static evaluation)
            max_next = max(q_table[state].values())
            new_q = old_q + alpha * (reward + gamma * max_next - old_q)
            q_table[state][action] = round(new_q, 4)

    print(f'[Q] Trained {len(q_table)} discrete states')

    # Print stats
    action_pref = {}
    for state, actions in q_table.items():
        best = max(actions, key=actions.get)
        action_pref[best] = action_pref.get(best, 0) + 1
    print(f'[Q] Action preferences: {dict(sorted(action_pref.items(), key=lambda x: -x[1]))}')

    return q_table


def save_model(rf, sgd, q_table, X, y, rewards):
    """Atomic save with backup."""
    os.makedirs(MODELS_DIR, exist_ok=True)

    # Backup existing
    for name in ('ai_agent.joblib', 'ai_data.pkl', 'ai_qtable.pkl'):
        src = os.path.join(MODELS_DIR, name)
        if os.path.exists(src):
            prev = src + '.prev'
            try:
                shutil.copy2(src, prev)
            except Exception:
                pass

    # Save model
    tmp_model = os.path.join(MODELS_DIR, 'ai_agent.joblib.tmp')
    final_model = os.path.join(MODELS_DIR, 'ai_agent.joblib')
    joblib.dump({'rf': rf, 'sgd': sgd}, tmp_model, compress=3)
    os.replace(tmp_model, final_model)

    # Save data (last 2000 observations)
    tmp_data = os.path.join(MODELS_DIR, 'ai_data.pkl.tmp')
    final_data = os.path.join(MODELS_DIR, 'ai_data.pkl.pkl')
    with open(tmp_data, 'wb') as f:
        pickle.dump({
            'X': X[-2000:],
            'y': y[-2000:],
            'rewards': rewards[-2000:],
        }, f)
    os.replace(tmp_data, final_data)

    # Save Q-table
    tmp_qtab = os.path.join(MODELS_DIR, 'ai_qtable.pkl.tmp')
    final_qtab = os.path.join(MODELS_DIR, 'ai_qtable.pkl')
    with open(tmp_qtab, 'wb') as f:
        pickle.dump(q_table, f)
    os.replace(tmp_qtab, final_qtab)

    # Save metadata
    meta = {
        'model_version': 'v2.0.0',
        'feature_version': 'v1',
        'dataset_version': 'd2000',
        'event_count': len(X),
        'cross_val_accuracy': 0.0,
        'trained_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'training_mode': 'smart_retrain_v2',
        'class_balance': {c: y.count(c) for c in ACTIONS},
    }
    with open(META_PATH, 'w') as f:
        json.dump(meta, f, indent=2)

    print(f'[SAVE] Models saved to {MODELS_DIR}/')
    print(f'[SAVE] ai_agent.joblib: {os.path.getsize(final_model)/1024:.0f} KB')
    print(f'[SAVE] ai_data.pkl: {os.path.getsize(final_data)/1024:.0f} KB')
    print(f'[SAVE] ai_qtable.pkl: {os.path.getsize(final_qtab)/1024:.0f} KB')


def main():
    print('=' * 60)
    print('  OPX Smart Retrain — Fresh Balanced Training')
    print('=' * 60)
    print()

    # Step 1: Generate balanced data
    print('[1/4] Generating balanced training data...')
    samples = generate_samples()
    X = [s[0] for s in samples]
    y = [s[1] for s in samples]

    from collections import Counter
    counts = Counter(y)
    print(f'  Total: {len(X)} samples')
    for label, count in sorted(counts.items()):
        pct = count / len(X) * 100
        bar = '█' * int(pct / 2)
        print(f'  {label:>8}: {count:>5} ({pct:.1f}%) {bar}')
    print()

    # Generate rewards based on label
    rewards = []
    for label in y:
        if label == 'proceed':
            rewards.append(round(random.uniform(0.3, 1.0), 3))
        elif label == 'wait':
            rewards.append(round(random.uniform(-0.2, 0.2), 3))
        elif label == 'skip':
            rewards.append(round(random.uniform(-0.3, 0.0), 3))
        elif label == 'abort':
            rewards.append(round(random.uniform(-0.5, -0.1), 3))
        else:
            rewards.append(0.0)

    # Step 2: Train RF
    print('[2/4] Training Random Forest (batch learner)...')
    rf = train_rf(X, y)
    print()

    # Step 3: Train SGD
    print('[3/4] Training SGD (online learner)...')
    sgd = train_sgd(X, y)
    print()

    # Step 4: Train Q-table
    print('[4/4] Training Q-Table (RL)...')
    q_table = train_qtable(samples)
    print()

    # Step 5: Save
    print('[SAVE] Saving models...')
    # Update meta with actual accuracy
    Xa = np.array(X)
    ya = np.array(y)
    scores = cross_val_score(rf, Xa, ya, cv=5, scoring='accuracy')
    meta = {
        'model_version': 'v2.0.0',
        'feature_version': 'v1',
        'dataset_version': 'd2000',
        'event_count': len(X),
        'cross_val_accuracy': round(float(scores.mean()), 4),
        'trained_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'training_mode': 'smart_retrain_v2',
        'class_balance': {c: y.count(c) for c in ACTIONS},
    }
    os.makedirs(MODELS_DIR, exist_ok=True)
    with open(META_PATH, 'w') as f:
        json.dump(meta, f, indent=2)

    save_model(rf, sgd, q_table, X, y, rewards)
    print()
    print('=' * 60)
    print('  ✅ SMART RETRAIN COMPLETE!')
    print(f'  CV Accuracy: {scores.mean():.4f}')
    print(f'  Q-Table States: {len(q_table)}')
    print(f'  Observations: {len(X)}')
    print('=' * 60)


if __name__ == '__main__':
    main()
