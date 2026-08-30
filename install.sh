#!/bin/bash
# ================================================================
#  OPXoneshot (wifi4) — One-File Universal Installer
#
#  Usage:  curl -fsSL <url>/install.sh -o install.sh && sudo bash install.sh
#
#  This script is SELF-CONTAINED. It downloads everything from GitHub:
#    - oneshot.py + source files (raw GitHub)
#    - AI brain model (GitHub Releases)
#    - System packages (apt/apk/pacman/dnf)
#    - Python ML packages (pip)
#
#  No git clone needed. No repo needed. Just this one file.
#  Supports: Alpine, Kali, Debian, Ubuntu, Parrot, Arch, Fedora/CentOS
# ================================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

info()  { echo -e "${CYAN}[*]${NC} $1"; }
ok()    { echo -e "${GREEN}[+]${NC} $1"; }
warn()  { echo -e "${YELLOW}[!]${NC} $1"; }
err()   { echo -e "${RED}[x]${NC} $1"; exit 1; }

# --- Root check ---
if [ "$(id -u)" -ne 0 ]; then
    err "Run as root: sudo bash install.sh"
fi

# --- GitHub source ---
REPO="OPX-Aminul/OPXoneshot"
RAW="https://raw.githubusercontent.com/${REPO}/main"
RELEASES="https://api.github.com/repos/${REPO}/releases"

# --- Install directory ---
INSTALL_DIR="/opt/oneshot-ai"
WIFI4_BIN="/usr/local/bin/wifi4"

# ================================================================
# 1. Detect distro
# ================================================================
detect_distro() {
    DISTRO="unknown"
    if [ -f /etc/alpine-release ]; then
        DISTRO="alpine"
    elif [ -f /etc/os-release ]; then
        . /etc/os-release
        case "$ID" in
            kali)       DISTRO="kali" ;;
            debian)     DISTRO="debian" ;;
            ubuntu)     DISTRO="ubuntu" ;;
            parrot)     DISTRO="parrot" ;;
            fedora)     DISTRO="fedora" ;;
            centos|rhel) DISTRO="centos" ;;
            arch|manjaro) DISTRO="arch" ;;
        esac
    elif [ -f /etc/debian_version ]; then
        DISTRO="debian"
    fi
    ok "Detected: ${DISTRO}"
}

# ================================================================
# 2. Install system packages
# ================================================================
install_packages() {
    info "Installing system packages..."

    _install_alpine() {
        ALPINE_VER=$(cat /etc/alpine-release 2>/dev/null || echo "3.18")
        ALPINE_MAJOR=$(echo "$ALPINE_VER" | cut -d. -f1,2)
        if ! grep -q "community" /etc/apk/repositories 2>/dev/null; then
            echo "https://dl-cdn.alpinelinux.org/alpine/v${ALPINE_MAJOR}/community" >> /etc/apk/repositories
        fi
        apk update || true
        for pkg in python3 py3-pip wireless-tools iw wpa_supplicant \
                   build-base python3-dev libnl3-dev libpcap-dev \
                   git curl bash sudo procps; do
            apk add --no-cache "$pkg" 2>/dev/null && ok "  $pkg" || warn "  $pkg (not available)"
        done
    }

    _install_debian() {
        apt-get update -y || true
        for pkg in python3 python3-pip python3-venv python3-dev \
                   wireless-tools iw wpasupplicant \
                   libpcap-dev libnl-3-dev libnl-genl-3-dev \
                   build-essential git curl sudo procps; do
            apt-get install -y "$pkg" 2>/dev/null && ok "  $pkg" || warn "  $pkg (not available)"
        done
        # Kali/Parrot extras
        if [ "$DISTRO" = "kali" ] || [ "$DISTRO" = "parrot" ]; then
            for pkg in wash mdk4 reaver pixiewps aircrack-ng; do
                apt-get install -y "$pkg" 2>/dev/null && ok "  $pkg" || true
            done
        fi
    }

    _install_arch() {
        pacman -Syu --noconfirm python python-pip wireless_tools iw wpa_supplicant \
            libpcap libnl3 base-devel git curl sudo procps-ng 2>/dev/null \
            && ok "  base packages" || warn "  some packages failed"
    }

    _install_fedora() {
        MGR="dnf"; command -v dnf &>/dev/null || MGR="yum"
        $MGR install -y python3 python3-pip wireless-tools iw wpa_supplicant \
            libpcap-devel libnl3-devel gcc make git curl sudo procps-ng 2>/dev/null \
            && ok "  base packages" || warn "  some packages failed"
    }

    case "$DISTRO" in
        alpine)              _install_alpine ;;
        debian|ubuntu|kali|parrot) _install_debian ;;
        arch|manjaro)        _install_arch ;;
        fedora|centos)       _install_fedora ;;
        *)                   warn "Unknown distro, trying Debian..." ; _install_debian ;;
    esac

    # Python ML packages via pip
    info "Installing Python ML packages via pip..."
    pip3 install --break-system-packages scikit-learn numpy joblib 2>/dev/null \
        || pip3 install scikit-learn numpy joblib 2>/dev/null \
        || python3 -m pip install scikit-learn numpy joblib 2>/dev/null \
        || warn "pip install failed — install manually: pip3 install scikit-learn numpy joblib"
}

# ================================================================
# 3. Download ALL source files from GitHub (no git clone needed)
# ================================================================
download_source() {
    info "Downloading ALL OPXoneshot source files from GitHub..."
    mkdir -p "$INSTALL_DIR/models"

    # --- Core tool (single-file build: all src/* embedded inside) ---
    info "  [core] oneshot.py..."
    curl -fsSL "${RAW}/oneshot.py" -o "${INSTALL_DIR}/oneshot.py" \
        && ok "  oneshot.py (self-contained)" || err "  FAILED: oneshot.py"
    chmod +x "${INSTALL_DIR}/oneshot.py"

    # --- Data files ---
    info "  [data] Vulnerable devices list..."
    for f in vulnwsc_new.txt; do
        curl -fsSL "${RAW}/${f}" -o "${INSTALL_DIR}/${f}" 2>/dev/null \
            && ok "  ${f}" || warn "  ${f} (optional)"
    done

    # --- Knowledge base files ---
    info "  [knowledge] Knowledge bases..."
    for f in wifi_master_knowledge.py wps_knowledge_base.py cve_database.py \
             research_knowledge.py offensive_reasoning_engine.py; do
        curl -fsSL "${RAW}/${f}" -o "${INSTALL_DIR}/${f}" 2>/dev/null \
            && ok "  ${f}" || warn "  ${f} (optional)"
    done

    # --- Training & build scripts ---
    info "  [scripts] Training & build scripts..."
    for f in smart_retrain.py model_build.py mega_train.py \
             train_master.py benchmark.py supabase_setup.sql; do
        curl -fsSL "${RAW}/${f}" -o "${INSTALL_DIR}/${f}" 2>/dev/null \
            && ok "  ${f}" || warn "  ${f} (optional)"
    done

    # --- Requirements ---
    info "  [config] requirements.txt..."
    curl -fsSL "${RAW}/requirements.txt" -o "${INSTALL_DIR}/requirements.txt" 2>/dev/null \
        && ok "  requirements.txt" || warn "  requirements.txt (optional)"

    # --- Model metadata (if exists in repo) ---
    mkdir -p "${INSTALL_DIR}/models"
    curl -fsSL "${RAW}/models/model_metadata.json" -o "${INSTALL_DIR}/models/model_metadata.json" 2>/dev/null \
        && ok "  models/model_metadata.json" || true

    # --- Count downloaded files ---
    FILE_COUNT=$(find "$INSTALL_DIR" -maxdepth 1 -type f | wc -l)
    ok "Downloaded ${FILE_COUNT} source files to ${INSTALL_DIR}"
}

# ================================================================
# 4. Download AI brain model from GitHub Releases
# ================================================================
download_models() {
    info "Downloading latest AI brain model from GitHub Releases..."
    MODELS_DIR="${INSTALL_DIR}/models"
    mkdir -p "$MODELS_DIR"

    # Get latest release
    LATEST_URL="${RELEASES}/latest"
    TAG=$(curl -fsSL "$LATEST_URL" 2>/dev/null | grep -o '"tag_name": *"[^"]*"' | head -1 | cut -d'"' -f4)

    if [ -z "$TAG" ]; then
        TAG="model-latest"
    fi
    info "  Release: ${TAG}"

    # Get release assets
    ASSETS=$(curl -fsSL "${RELEASES}/tags/${TAG}" 2>/dev/null | grep -o '"browser_download_url": *"[^"]*"' | cut -d'"' -f4)

    if [ -z "$ASSETS" ]; then
        warn "  No release assets found — models will train on first run"
        return 0
    fi

    DOWNLOADED=0
    while IFS= read -r URL; do
        [ -z "$URL" ] && continue
        FILENAME=$(basename "$URL")
        info "  Downloading ${FILENAME}..."
        if curl -fsSL -o "${MODELS_DIR}/${FILENAME}" "$URL" 2>/dev/null; then
            DOWNLOADED=$((DOWNLOADED + 1))
        else
            warn "  Failed: ${FILENAME}"
        fi
    done <<< "$ASSETS"

    ok "Downloaded ${DOWNLOADED} model files"
}

# ================================================================
# 5. Create global wifi4 + oneshot commands
# ================================================================
create_commands() {
    info "Creating global commands..."

    cat > "$WIFI4_BIN" << CMDEOF
#!/bin/bash
exec python3 ${INSTALL_DIR}/oneshot.py --ai "\$@"
CMDEOF
    chmod +x "$WIFI4_BIN"
    ok "wifi4 -> ${WIFI4_BIN}"

    ONESHOT_BIN="/usr/local/bin/oneshot"
    cat > "$ONESHOT_BIN" << CMDEOF
#!/bin/bash
exec python3 ${INSTALL_DIR}/oneshot.py "\$@"
CMDEOF
    chmod +x "$ONESHOT_BIN"
    ok "oneshot -> ${ONESHOT_BIN}"
}

# ================================================================
# 6. Verify installation
# ================================================================
verify_install() {
    info "Verifying installation..."
    PASS=0; FAIL=0
    for cmd in python3 iw curl; do
        command -v "$cmd" &>/dev/null && ok "  $cmd" && PASS=$((PASS+1)) || { warn "  $cmd NOT FOUND"; FAIL=$((FAIL+1)); }
    done
    python3 -c "import sklearn,numpy,joblib" 2>/dev/null && ok "  Python ML packages" && PASS=$((PASS+1)) || { warn "  Python ML packages missing"; FAIL=$((FAIL+1)); }
    [ -f "${INSTALL_DIR}/oneshot.py" ] && ok "  oneshot.py" && PASS=$((PASS+1)) || { warn "  oneshot.py missing"; FAIL=$((FAIL+1)); }
    [ -f "${INSTALL_DIR}/models/ai_agent.joblib" ] && ok "  AI brain model" && PASS=$((PASS+1)) || warn "  AI model (will train on first run)"
    command -v wifi4 &>/dev/null && ok "  wifi4 command" && PASS=$((PASS+1)) || { warn "  wifi4 NOT FOUND"; FAIL=$((FAIL+1)); }
    echo ""
    ok "Verification: ${PASS} passed, ${FAIL} warnings"
}

# ================================================================
# MAIN
# ================================================================
echo ""
echo -e "${CYAN}╔══════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║  OPXoneshot (wifi4) — One-File Universal Installer  ║${NC}"
echo -e "${CYAN}║  No git clone needed. Just this script.             ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════════════╝${NC}"
echo ""

detect_distro
install_packages
download_source
download_models
create_commands
verify_install

echo ""
ok "═══════════════════════════════════════════════════"
ok "Installation complete!"
ok ""
ok "Run from anywhere:  wifi4"
ok "Or:                 oneshot --ai"
ok "Location:           ${INSTALL_DIR}/"
ok "═══════════════════════════════════════════════════"
echo ""
