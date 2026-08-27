# OneShot-Extended (OPX)

**AI-powered WPS vulnerability testing and offline PIN analysis framework.**

A single-file, self-contained WPS (Wi-Fi Protected Setup) auditing tool with embedded Artificial Intelligence that autonomously scans, selects, and attacks WiFi networks. The AI learns from every attempt and improves over time.

---

## Features

- **Fully Autonomous AI** -- `wifi4` scans, lists networks, user selects, AI attacks automatically
- **Pre-trained Model** -- RF + SGD + Q-Learning (115 states, 2000+ episodes trained)
- **Smart Auto-Attack Chain** -- Vuln list PIN -> Pixie Dust -> Online bruteforce
- **13-Feature Vector** -- Signal, WPS version, locked state, timeouts, message counts, etc.
- **Online Learning** -- AI improves with every attack attempt
- **Auto Dependency Installer** -- Installs pixiewps, reaver, bully, iw automatically
- **Global Command** -- `wifi4` works from any directory after one-time install
- **WPS State Diagnostics** -- Checks if WPS is enabled, locked, or disabled before attacking
- **Community Learning Sync** -- Auto-syncs attack data + model across all users (Supabase + GitHub), zero flags
- **Safety & Robustness** -- Event validation, noise/poison filtering, 100MB footprint guard, atomic save + rollback, offline queue, concurrency lock
- **Golden Model CI** -- GitHub Actions rebuilds a clean shared model every 3 days
- **Single File Core** -- Everything in `oneshot.py` (5250+ lines)

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/OPX-Aminul/OPXoneshot.git
cd OPXoneshot

# 2. Install globally (one time)
sudo python3 oneshot.py --install

# 3. Run from anywhere
wifi4
```

---

## Usage

### AI Autonomous Mode (Recommended)

```bash
# From anywhere (after install)
wifi4

# Or directly
python3 oneshot.py --ai

# With specific interface
python3 oneshot.py --ai -i wlan0
```

**What happens:**
1. Auto-detects wireless interface
2. Scans all nearby WPS networks
3. Shows numbered list -- you select one
4. AI checks if it is in the vulnerable device list
5. If found -- uses the known PIN directly
6. If not found -- Pixie Dust attack -> Online bruteforce
7. AI decides at each phase whether to proceed, wait, skip, or abort
8. Model saves automatically (learns from every attempt)

### Manual Modes

```bash
# Check a router (no attack)
python3 oneshot.py --check BSSID

# Scan and select network
python3 oneshot.py -i wlan0

# Pixie Dust attack
python3 oneshot.py -i wlan0 -b BSSID -P

# Online bruteforce
python3 oneshot.py -i wlan0 -b BSSID -B

# Use specific PIN
python3 oneshot.py -i wlan0 -b BSSID -p 12345670

# Push button connect
python3 oneshot.py -i wlan0 -b BSSID --pbc

# Show all networks (including WPS disabled)
python3 oneshot.py -i wlan0 -a

# Kill interfering processes
python3 oneshot.py -i wlan0 -k

# Loop mode
python3 oneshot.py -i wlan0 -l
```

### Install / Uninstall

```bash
# Install globally
sudo python3 oneshot.py --install

# This creates:
#   /usr/local/bin/wifi4       (AI autonomous command)
#   /usr/local/bin/oneshot     (general command)
#   /usr/local/bin/oneshot-ai/ (script + models)
```

### Community Model / Training Data

Every time you run `wifi4` (or `oneshot.py`), the AI **automatically**:

1. **Learns the newest shared model** from GitHub (`git fetch` + checkout latest `models/`)
2. **Uploads queued offline events** (durable JSONL queue — survives crashes / no-network)
3. **Pushes your fresh attack data** to the Supabase community store (idempotent `event_id`)
4. **Pulls only the new community rows** since your last sync and learns them in ~1 second (incremental SGD — no full model download)
5. **Filters noise / poisoning** on ingest (low-quality events rejected; GC keeps high-value + rare + recent)

No flags, no user action. New users who clone the repo immediately get the latest trained model.

Background (throttled every 30 min, once-per-day git push): the model is fully retrained on the merged community data and pushed back to GitHub automatically.

#### Safety & Robustness (built-in, no config)

| Protection | Behavior |
|---|---|
| Event validation | Rejects NaN/inf/impossible signal/reward/bad action |
| Noise / poison filter | Drops events with quality score < 0.25 on pull |
| Footprint guard | Warns at 80 MB, critical 90 MB, hard-cap 100 MB |
| Garbage collection | Smart retention (high-quality + rare-success + recent), not blind top-N |
| Atomic save | Write to `.tmp`, validate, `os.replace`; keeps `.prev` for rollback |
| Offline queue | Durable JSONL; replays on reconnect (two-way sync) |
| Concurrency lock | Exclusive `.sync.lock` prevents overlapping syncs |
| Retry / backoff | Exponential backoff on transient HTTP failures |
| Duplicate guard | `event_id` upsert + dedup set (idempotent) |
| Versioning | `models/model_metadata.json` tracks model/dataset/feature versions |

#### Privacy / Credentials

- The **anon** Supabase key is used by default (safe for client insert/select).
- The **service_role** key (cross-user reads for the golden model) is **never** in source — it is injected via the `SUPABASE_SERVICE_ROLE_KEY` GitHub secret.
- `.env` is git-ignored; local dev loads it via `_load_env_file()`.

Explicit commands still available:

```bash
# Export your training data (share on GitHub so others learn from it)
python3 oneshot.py --export

# Import another user's training data (merge into your model)
python3 oneshot.py --import-data training_data_20260827.json

# Pull the latest community model from GitHub
python3 oneshot.py --pull-model

# Push your trained model back to GitHub
python3 oneshot.py --push-model

# A/B training profiles (how aggressive the AI explores)
python3 oneshot.py --ai --profile conservative
python3 oneshot.py --ai --profile balanced     # default
python3 oneshot.py --ai --profile aggressive
```

Supabase community sync:

```bash
python3 oneshot.py --sync          # push local -> pull community -> retrain -> git push
python3 oneshot.py --push-data     # only upload local training log
python3 oneshot.py --pull-data     # only download new community rows
```

Every user's `record()` calls are saved to `~/.OneShot-Extended/training_log.json`
with a unique user id. Data flows to the shared Supabase table + GitHub model
so everyone's model improves from everyone's experience.

#### One-time setup (owner)

```bash
# 1. Create the Supabase table (run once in Supabase SQL Editor)
#    -> see supabase_setup.sql

# 2. Add GitHub repo secrets so the nightly golden-model build can read all rows:
#    SUPABASE_URL              = https://oenckshhftqjjwhngxzo.supabase.co
#    SUPABASE_SERVICE_ROLE_KEY = <service_role key from Supabase dashboard>
```

---

## How the AI Works

### Architecture

```
+-------------------+
|   User selects    |
|   network         |
+--------+----------+
         |
    +----v----+
    | AIAgent |
    +----+----+
         |
    +----v----------+----------+----------+
    |               |          |          |
    |  RF Model     | SGD      | Q-Table  |
    |  (batch, 0.4) | (online, | (RL,     |
    |               |  0.3)    |  0.3)    |
    +----+----------+----+-----+----+-----+
         |               |          |
         +-------+-------+----------+
                 |
         +-------v--------+
         |  Vote Weighted  |
         |  Decision       |
         +-------+--------+
                 |
    +------------+------------+
    |            |            |
proceed       wait/skip     abort
```

### 13 Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | signal | WiFi signal strength (dBm) |
| 2 | wps_version | WPS protocol version |
| 3 | wps_locked | Is WPS setup locked? |
| 4 | is_vulnerable | Known vulnerable device? |
| 5 | attempt | Current attempt number |
| 6 | timeouts | Consecutive timeouts |
| 7 | resp_delay | Response delay (seconds) |
| 8 | m_msgs | M-message count (WPS progress) |
| 9 | fails | Failed attempts so far |
| 10 | sig_ok | Signal above threshold? |
| 11 | oui | OUI match from vuln list? |
| 12 | frame_loss | Frame loss ratio |
| 13 | hist_locks | Historical lock events |

### Training

The model is pre-trained with 2000+ episodes across 25 scenarios:
- **Vuln list attacks** (5 scenarios) -- Easy/Medium/Tight/Locked/Disabled
- **Pixie Dust attacks** (5 scenarios) -- Real vuln/Marginal/Weak/Not vuln/Locked
- **Bruteforce attacks** (5 scenarios) -- Good/Fair/Weak/Locked/Timeout
- **Exhaustive attacks** (5 scenarios) -- All correct/Marginal/Bad/Lockout/Disabled
- **Adversarial edge cases** (5 scenarios) -- Traps and confusion patterns

### Decision Flow

```
1. AI checks vuln list -> found? -> Try PIN -> Success? Done.
2. Not found or PIN failed -> AI decides: Pixie Dust?
3. Pixie Dust failed -> AI decides: Bruteforce?
4. Each phase: AI considers signal, locks, timeouts, history
5. AI can abort early if success probability is too low
6. Every attempt is recorded -> model improves over time
```

---

## File Structure

```
OPXoneshot/
+-- oneshot.py                       # Main script (5250+ lines, everything included)
+-- model_build.py                   # Standalone golden-model trainer (CI)
+-- supabase_setup.sql               # One-time Supabase schema (event_id + quality)
+-- requirements.txt                 # scikit-learn, joblib, numpy
+-- models/
|   +-- ai_agent.joblib              # RF + SGD trained models (compressed)
|   +-- ai_data.pkl                  # Observations
|   +-- ai_qtable.pkl                # Q-table
|   +-- model_metadata.json          # Model/dataset/feature versioning
+-- .github/workflows/
|   +-- nightly-model-build.yml      # Cron every 3 days -> rebuild golden model
+-- wifi4                            # Shortcut script
+-- README.md                        # This file
+-- .gitignore
```

---

## Requirements

- **OS:** Linux (Kali, Parrot, Ubuntu, Debian)
- **Python:** 3.8+
- **Root access:** Required
- **WiFi adapter:** Supports monitor mode
- **Auto-installed:** pixiewps, reaver, bully, iw, scikit-learn, numpy, joblib

---

## All Flags

```
Required:
  -i, --interface      Wireless interface name
  -b, --bssid          Target AP BSSID

Check Mode:
  -C, --check BSSID    Check router against vuln list (no attack)

Attack Modes:
  -p, --pin PIN        Use specific PIN
  -N, --null-pin       Use null PIN
  -P, --pixie-dust     Pixie Dust attack
  -B, --bruteforce     Online bruteforce
  --pbc                Push button connect

AI Mode:
  --ai                 Full autonomous mode (scan -> select -> attack)

Install:
  --install            Install wifi4 globally to /usr/local/bin

Optional:
  -k, --kill           Kill interfering processes
  -r, --restore        Restore processes on exit
  -w, --write          Save credentials to file
  -l, --loop           Run in loop
  -c, --clear          Clear screen on scan
  -a, --all            Show all networks (including WPS off)
  -d, --delay SEC      Delay between pin attempts
  -t, --timeout SEC    Timeout for WPS lock retry

Advanced:
  -F, --pixie-force    Pixiewps --force option
  -S, --show-pixie     Print pixiewps command
  -I, --iface-down     Disable interface on exit
  -M, --mtk-wifi       MediaTek WiFi driver toggle
  -D, --dont-touch-settings   Skip Android WiFi settings
  --reverse-scan       Reverse network list order
  --vuln-list FILE     Custom vulnerable devices file
  -v, --verbose        Verbose output
  -h, --help           Show help
```

---

## How It Works (Simple)

```
$ wifi4

[*] Using interface: wlan0
[*] Scanning for WPS networks...

  #  BSSID               CH  SIGNAL  WPS  LOCK  ESSID
  1  AA:BB:CC:DD:EE:FF    6   -42    v2   No    MyWiFi
  2  11:22:33:44:55:66   11   -58    v1   Yes   Neighbor
  3  DE:AD:BE:EF:00:11    1   -71    v2   No    CafeWiFi

Select target: 1

[*] Selected: MyWiFi (AA:BB:CC:DD:EE:FF)
    Signal: -42 dBm | WPS v2.0 | Locked: False

[AI] Phase 1: Checking vulnerable list...
[AI] Decision: proceed
[AI] Trying PIN: 12345670 (Common default)
[AI] SUCCESS! PIN: 12345670

[AI] Model saved: AI Agent ready (RF, SGD, Q(115), 500 obs)
```

---

## Community Learning Sync (Optional)

The tool can share anonymized attack-outcome data and a shared model across
users via **GitHub** (model binaries) and **Supabase** (event rows). This is
fully opt-in and runs silently in the background; it never interferes with
attacks.

- Events are pushed with an `event_id` (idempotent) and `quality` score.
- Only lightweight rows are synced, not full models.
- The shared "golden" model is rebuilt periodically by CI and committed to
  `models/`.

### One-time setup (owner)

1. Create the Supabase table once in the dashboard by running `supabase_setup.sql`.
2. Add repo **Secrets** so the nightly workflow can read all rows:
   - `SUPABASE_URL` = `https://oenckshhftqjjwhngxzo.supabase.co`
   - `SUPABASE_SERVICE_ROLE_KEY` = the service_role key from the Supabase dashboard

### Files added for this feature

```
model_build.py                  # Standalone golden-model trainer (run by CI)
supabase_setup.sql              # One-time Supabase schema (event_id + quality)
requirements.txt                # scikit-learn, joblib, numpy
.github/workflows/nightly-model-build.yml  # Cron -> rebuild golden model
```

> The privileged `service_role` key is never hardcoded in source; it is
> supplied only through the GitHub secret above. The public `anon` key is used
> for client-side inserts.

---

## Credits

- **Original:** [_skipmarket/OneShot](https://github.com/skipmarket/OneShot)
- **Extended:** OneShot-Extended with AI Agent, smart auto-attack, WPS diagnostics
- **AI:** Hybrid RF + SGD + Q-Learning ensemble
- **Copyright:** (C) 2026 chkndrp

---

## License

For authorized security testing only. Use responsibly.
