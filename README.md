# OneShot-Extended (OPX)

**WPS vulnerability testing and offline PIN analysis framework.**

A single-file, self-contained WPS (Wi-Fi Protected Setup) auditing tool that combines
pixie-dust offline attacks, PIN algorithm derivation from OUI vendor lists, online
bruteforce, and over-the-air WPS capability diagnostics — all in one `oneshot.py`.

Forked and extended from the original OneShot project with additional features:
`--check` offline/live diagnosis, `--all` network visibility, WPS state probing,
automatic disabled-WPS detection, and a unified single-file architecture.

> **This tool is intended exclusively for authorized security testing and research.
> Unauthorized access to computer networks is illegal.**

---

## Features

### Core Attack Modes

| Flag | Mode | Description |
|------|------|-------------|
| `-P` | Pixie Dust | Offline WPS PIN recovery via weak PRNG nonce analysis |
| `-B` | Online Bruteforce | Full 8-digit WPS PIN brute-force (up to ~11,000 attempts with smart filtering) |
| `-p PIN` | Known PIN | Test a specific PIN (from prediction, leaked database, or manual input) |
| `-N` | Null PIN | Try the null (all-zeros) PIN — effective on some early WPS implementations |
| `--pbc` | Push Button | WPS Push Button Connect (PBC) mode |

### WPS State Diagnostics (New)

| Flag | Function | Description |
|------|----------|-------------|
| `-C BSSID` | `--check` (offline) | Match a BSSID against the 612-entry vulnerable device list + check for previously saved PINs — no interface/root required |
| `-C BSSID -i wlan0` | `--check` (live) | Same as above + active `iw scan` to report the AP's actual over-the-air WPS state: **enabled / locked / disabled / not found** |
| `-a` | `--all` | Show ALL networks in the scan table including those with WPS **disabled/absent** (displayed in gray as `OFF`), instead of filtering them out |

### Pre-flight and Robustness

- **Pre-flight WPS probe**: when `-b BSSID` is given without a prior scan, the tool
  automatically probes the target AP to report its WPS state before launching an
  attack. A visible AP without a WPS IE gets an immediate warning instead of
  silently hanging.
- **Disabled-WPS auto-abort**: if an AP never responds to any WPS protocol message
  after 3 consecutive timeouts, the tool aborts with a clear diagnostic message
  instead of looping indefinitely.

### Additional Features

- `-i` / `-b` selection: scan all networks and interactively choose, or target a
  specific BSSID directly
- `-k` / `-r`: kill/restore interfering wireless processes (NetworkManager,
  wpa_supplicant, etc.)
- `-l`: loop mode — re-scan after each attempt
- `-w`: write recovered credentials to file
- `-S`: show pixiewps command and raw data
- `-F`: force pixiewps bruteforce mode
- `-v`: verbose output
- OUI-based PIN prediction from 612 known vulnerable device algorithms
  (generator.py)
- WPS lockout awareness — auto-retry with configurable timeout on locked APs
- Android and MediaTek Wi-Fi driver support

---

## Single-File Architecture

The entire project lives in **`oneshot.py`** — one file, no external modules.

Original source files (`src/args.py`, `src/utils.py`, `src/wifi/scanner.py`,
`src/wps/connection.py`, `src/wps/pixiewps.py`, `src/wps/generator.py`,
`src/wps/bruteforce.py`, `src/wifi/android.py`, `src/wifi/collector.py`,
`src/logger.py`, `ose.py`) and the 612-entry `vulnwsc.txt` vulnerable devices list
are all embedded and bootstrapped via an in-memory `_SrcModule` shim that
reconstructs the `src.*` package hierarchy at import time — preserving the original
code 100% verbatim.

---

## Requirements

### System Dependencies

The following must be installed and available in `$PATH`:

| Dependency | Purpose |
|------------|---------|
| `iw` | Wireless interface scanning and control |
| `wpa_supplicant` | WPS protocol communication (must be compiled with `CONFIG_WPS=y`) |
| `pixiewps` | Offline Pixie Dust PIN computation |
| `ip` | Network interface management |
| Python >= 3.10 | Script interpreter |

### Python

No `pip install` required. Standard library only.

---

## Setup

### 1. Install System Dependencies

**Debian / Ubuntu / Kali:**

```bash
sudo apt update
sudo apt install -y iw wpa_supplicant pixiewps iproute2 python3
```

**Arch Linux:**

```bash
sudo pacman -S iw wpa_supplicant pixiewps iproute2 python
```

**Termux (Android):**

```bash
pkg install root-repo
pkg install iw wpa_supplicant pixiewps iproute2 python
```

### 2. Verify pixiewps Supports WPS

```bash
pixiewps --help 2>&1 | head -5
```

If pixiewps is not available, build from source:

```bash
git clone https://github.com/wiire-a/pixiewps.git
cd pixiewps
make
sudo make install
```

### 3. Verify wpa_supplicant Has WPS Support

```bash
wpa_supplicant -h 2>&1 | grep -i wps
```

You should see `WPS` in the supported commands. If not, rebuild with:

```bash
CONFIG_WPS=y make
```

### 4. Download oneshot.py

```bash
wget https://raw.githubusercontent.com/yourusername/OPXoneshot/main/oneshot.py
chmod +x oneshot.py
```

Or clone:

```bash
git clone https://github.com/yourusername/OPXoneshot.git
cd OPXoneshot
```

---

## Usage

### Basic Pixie Dust Attack (scan and select)

```bash
sudo python3 oneshot.py -i wlan0 -P
```

### Target a Specific BSSID with Pixie Dust

```bash
sudo python3 oneshot.py -i wlan0 -b AA:BB:CC:11:22:33 -P
```

### Online Brute-force (full 8-digit PIN search)

```bash
sudo python3 oneshot.py -i wlan0 -b AA:BB:CC:11:22:33 -B
```

### Test a Known PIN

```bash
sudo python3 oneshot.py -i wlan0 -b AA:BB:CC:11:22:33 -p 12345670
```

### WPS Push Button Connect

```bash
sudo python3 oneshot.py -i wlan0 --pbc
```

### Offline BSSID Check (no root or interface needed)

```bash
python3 oneshot.py --check AA:BB:CC:11:22:33
```

Output:
```
[*] Checking AA:BB:CC:11:22:33 against the vulnerable lists...
[+] IN the vulnerable list: 3 known vulnerable device algorithm(s) match this router:
[*]   - pinDLink   D-Link PIN (probable PIN: 76465154)
[*]   - pinDLink1  D-Link PIN+1 (probable PIN: 66672982)
[*] Recommended first PIN to try: 76465154
```

### Live WPS State Probe (offline check + over-the-air scan)

```bash
sudo python3 oneshot.py --check AA:BB:CC:11:22:33 -i wlan0
```

Output (if WPS is disabled on the AP):
```
[*] Checking AA:BB:CC:11:22:33 against the vulnerable lists...
[*] Probing AA:BB:CC:11:22:33 over the air (interface: wlan0)...
[-] AP not observed in the scan — out of range, hidden, or on another channel
```

Or:
```
[-] Over the air: WPS is DISABLED on this AP (no WPS IE broadcast).
    WPS-based attacks are not possible while it stays off —
    even a derived/predicted PIN cannot be used
```

### Scan All Networks (Including WPS-Disabled)

```bash
sudo python3 oneshot.py -i wlan0 -a
```

Displays all visible APs, with WPS-disabled ones shown in **gray** as `OFF` in the
`Ver.` column.

### Kill Interfering Processes + Loop Mode

```bash
sudo python3 oneshot.py -i wlan0 -k -P -l
```

### Verbose + Write Results

```bash
sudo python3 oneshot.py -i wlan0 -b AA:BB:CC:11:22:33 -P -v -w
```

---

## Command Reference

```
usage: oneshot.py [-h] [-i IFACE] [-b BSSID] [-C BSSID] [-p PIN] [-N] [-P] [-B]
                  [--pbc] [-k] [-r] [-w] [-l] [-c] [-a] [-d DELAY] [-t TIMEOUT]
                  [-F] [-S] [-I] [-M] [-D] [--reverse-scan] [--vuln-list FILE] [-v]
```

### Required Arguments

| Flag | Description |
|------|-------------|
| `-i`, `--interface` | Wireless interface name (e.g., `wlan0`). Not required when using `-C` alone. |
| `-b`, `--bssid` | Target AP MAC address. If omitted, a scan + interactive selection is performed. |

### Check Mode (No Attack)

| Flag | Description |
|------|-------------|
| `-C`, `--check BSSID` | Check a BSSID against the vulnerable list and saved data. Add `-i` to also probe the AP over the air. |

### Attack Modes (mutually exclusive)

| Flag | Description |
|------|-------------|
| `-p`, `--pin PIN` | Use the specified PIN |
| `-N`, `--null-pin` | Use null (all-zeros) PIN |
| `-P`, `--pixie-dust` | Run Pixie Dust offline attack |
| `-B`, `--bruteforce` | Run online PIN brute-force |
| `--pbc` | WPS Push Button Connect |

### Optional Arguments

| Flag | Description |
|------|-------------|
| `-k`, `--kill` | Kill processes interfering with the wireless interface |
| `-r`, `--restore` | Restore killed processes on exit (use with `-k`) |
| `-w`, `--write` | Write credentials to file on success |
| `-l`, `--loop` | Re-scan and retry in a loop |
| `-c`, `--clear` | Clear the screen before each scan |
| `-a`, `--all` | Show all networks including WPS-disabled (gray/`OFF`) |
| `-d`, `--delay` | Delay between brute-force pin attempts (default: 0) |
| `-t`, `--timeout` | Timeout for retrying after WPS lock (default: 60s) |

### Advanced Arguments

| Flag | Description |
|------|-------------|
| `-F`, `--pixie-force` | Run pixiewps with `--force` (full bruteforce range) |
| `-S`, `--show-pixie` | Print pixiewps command and related data |
| `-I`, `--iface-down` | Down the interface on exit |
| `-M`, `--mtk-wifi` | Activate MediaTek Wi-Fi interface driver on startup |
| `-D`, `--dont-touch-settings` | Don't touch Android Wi-Fi settings |
| `--reverse-scan` | Reverse network list order (small displays) |
| `--vuln-list FILE` | Custom vulnerable devices list file |
| `-v`, `--verbose` | Verbose output |

---

## How It Works

### Pixie Dust Attack

1. Connect to the target AP via WPS
2. Capture the EAPOL WPS exchange (PKE, PKR, E-S1, E-S2, E-Hash1, E-Hash2, AuthKey)
3. Run `pixiewps` offline to brute-force the PIN from weak router-generated nonces
4. Reconnect with the recovered PIN to extract the WPA PSK

**Affected routers**: Those using predictable PRNGs for WPS nonces
(Ralink/eCos, Realtek RTL819x, Broadcom, D-Link, and others — 612 known vulnerable
devices in the embedded list).

### OUI-Based PIN Prediction

The `generator.py` module contains 8+ algorithms that predict WPS PINs based on
the router's MAC address (OUI prefix). For vulnerable vendors, the PIN is often
derived from a deterministic formula — no attack traffic needed.

### WPS State Classification

The new `classifyWpsState()` / `probeWpsState()` functions parse `iw scan` output
to determine whether a target AP:

- **Enabled**: WPS IE present in beacon/probe response, no lock flag
- **Locked**: WPS IE present, but AP Setup Locked flag set (temporary lockout)
- **Disabled**: AP is visible but does not broadcast any WPS IE (firmware-level off)
- **Unknown**: AP not observed or insufficient data

---

## WPS Disabled — Why It Cannot Be Bypassed

If a router has its WPS feature turned **OFF** in firmware, the WPS protocol state
machine is never instantiated on the AP. There is no WPS Registrar/Enrollee service
running to respond to any client-side probe or manipulation. This means:

- **No protocol trick** can start an un-started state machine
- **Deauthentication frames** do not toggle firmware feature flags
- **UPnP WPS PIN disclosure** (Viehbock 2011) only leaks the PIN — it does not
  re-enable WPS, and is typically also disabled when WPS is off
- **WPS lockout bypass** (MAC spoofing/deauth reset) only applies to temporary
  lockout, not firmware-level disabling

The **only** scenario where WPS "appears disabled but still works" is a firmware bug
on certain cheap routers/ISP CPEs where the UI toggle does not actually disable the
WPS service. The `--probe` / `-C -i` diagnostics detect this by checking the actual
over-the-air WPS IE.

---

## File Structure

```
oneshot.py          # The entire tool (single file, ~3260 lines)
```

Everything is embedded: the 612-entry `vulnwsc.txt` vulnerable device list, all
original source modules (scanner, connection handler, pixiewps wrapper, WPS PIN
generator, bruteforcer, Android helpers, logger, utils), and the new diagnostic
functions — bootstrapped via an in-memory module shim at startup.

---

## Credits

- **Original OneShot** — WPS attack framework
- **Wi-PWN / pixiewps** — offline WPS analysis (wiire-a)
- **Reaver** — WPS brute-force reference implementation
- **Stefan Viehbock** — WPS vulnerability research ("Brute forcing Wi-Fi Protected Setup", 2011)
- **WPSpin generators** — OUI-based PIN prediction algorithms

---

## License

GNU General Public License v2.0 (GPLv2) — see the license header in `oneshot.py`.
