#!/bin/bash
# ================================================================
# OPXoneshot (wifi4) — Universal Linux Installer
# Detects distro and installs all dependencies automatically
# Supports: Alpine, Kali, Debian, Ubuntu, Parrot, Arch, Fedora
# ================================================================

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

info()  { echo -e "${CYAN}[*]${NC} $1"; }
ok()    { echo -e "${GREEN}[+]${NC} $1"; }
warn()  { echo -e "${YELLOW}[!]${NC} $1"; }
err()   { echo -e "${RED}[x]${NC} $1"; exit 1; }

# ── Must run as root ──────────────────────────────────────────
if [ "$(id -u)" -ne 0 ]; then
    err "This script must be run as root (use sudo or run as root user)."
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WIFI4_BIN="/usr/local/bin/wifi4"

# ── Distro Detection ─────────────────────────────────────────
detect_distro() {
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
            centos)     DISTRO="centos" ;;
            rhel)       DISTRO="centos" ;;
            arch|manjaro) DISTRO="arch" ;;
            *)          DISTRO="unknown" ;;
        esac
    elif [ -f /etc/debian_version ]; then
        DISTRO="debian"
    elif [ -f /etc/redhat-release ]; then
        DISTRO="centos"
    else
        DISTRO="unknown"
    fi
    ok "Detected distro: ${DISTRO}"
}

# ── Alpine Linux Setup ────────────────────────────────────────
setup_alpine() {
    info "Configuring Alpine Linux..."

    # Add community and edge/testing repos for extra packages
    if ! grep -q "community" /etc/apk/repositories 2>/dev/null; then
        info "Enabling community repository..."
        ALPINE_VER=$(cat /etc/alpine-release 2>/dev/null || echo "3.18")
        ALPINE_MAJOR=$(echo "$ALPINE_VER" | cut -d. -f1,2)
        echo "https://dl-cdn.alpinelinux.org/alpine/v${ALPINE_MAJOR}/community" >> /etc/apk/repositories
    fi

    if ! grep -q "testing" /etc/apk/repositories 2>/dev/null; then
        info "Enabling edge/testing repository..."
        ALPINE_VER=$(cat /etc/alpine-release 2>/dev/null || echo "3.18")
        ALPINE_MAJOR=$(echo "$ALPINE_VER" | cut -d. -f1,2)
        echo "https://dl-cdn.alpinelinux.org/alpine/v${ALPINE_MAJOR}/testing" >> /etc/apk/repositories
    fi

    info "Running apk update..."
    apk update

    info "Installing packages for Alpine Linux..."
    apk add --no-cache \
        python3 \
        py3-pip \
        py3-scikit-learn \
        py3-numpy \
        py3-joblib \
        wireless-tools \
        iw \
        wpa_supplicant \
        libnl3-dev \
        build-base \
        python3-dev \
        git \
        curl \
        bash \
        sudo \
        procps \
        aircrack-ng \
        reaver \
        pixiewps \
        bulk_extractor \
        libpcap-dev

    # Install bully if not in repos
    if ! command -v bully &>/dev/null; then
        warn "bully not in Alpine repos, building from source..."
        apk add --no-cache libpcap-dev libnl3-dev
        cd /tmp
        git clone https://github.com/aanarchyy/bully.git
        cd bully/src
        make -j"$(nproc)"
        cp bully /usr/local/bin/
        cd /
        rm -rf /tmp/bully
        ok "bully installed from source"
    fi
}

# ── Debian/Kali/Ubuntu/Parrot Setup ──────────────────────────
setup_debian() {
    info "Updating package lists..."
    apt-get update -y

    info "Installing packages for Debian-based system..."
    apt-get install -y \
        python3 \
        python3-pip \
        python3-venv \
        python3-dev \
        python3-scikit-learn \
        python3-numpy \
        python3-joblib \
        wireless-tools \
        iw \
        wpa_supplicant \
        libpcap-dev \
        libnl-3-dev \
        libnl-genl-3-dev \
        build-essential \
        git \
        curl \
        sudo \
        procps \
        aircrack-ng \
        reaver \
        pixiewps \
        bulk-extractor

    # Install bully if not available
    if ! command -v bully &>/dev/null; then
        if apt-cache show bully &>/dev/null 2>&1; then
            apt-get install -y bully
        else
            warn "bully not in repos, building from source..."
            cd /tmp
            git clone https://github.com/aanarchyy/bully.git
            cd bully/src
            make -j"$(nproc)"
            cp bully /usr/local/bin/
            cd /
            rm -rf /tmp/bully
            ok "bully installed from source"
        fi
    fi

    # Kali-specific tools
    if [ "$DISTRO" = "kali" ] || [ "$DISTRO" = "parrot" ]; then
        info "Installing additional pentest tools for ${DISTRO}..."
        apt-get install -y \
            wash \
            reaver \
            pixiewps \
            bully \
            mdk4 \
            hostapd-wpe 2>/dev/null || true
    fi
}

# ── Arch/Manjaro Setup ───────────────────────────────────────
setup_arch() {
    info "Installing packages for Arch Linux..."
    pacman -Syu --noconfirm \
        python \
        python-pip \
        python-scikit-learn \
        python-numpy \
        python-joblib \
        wireless_tools \
        iw \
        wpa_supplicant \
        libpcap \
        libnl3 \
        base-devel \
        git \
        curl \
        sudo \
        procps-ng \
        reaver \
        pixiewps \
        aircrack-ng

    # Install bully from AUR or build
    if ! command -v bully &>/dev/null; then
        warn "bully not found, building from source..."
        cd /tmp
        git clone https://github.com/aanarchyy/bully.git
        cd bully/src
        make -j"$(nproc)"
        cp bully /usr/local/bin/
        cd /
        rm -rf /tmp/bully
        ok "bully installed from source"
    fi
}

# ── Fedora/CentOS Setup ─────────────────────────────────────
setup_fedora() {
    info "Installing packages for Fedora/CentOS..."
    if command -v dnf &>/dev/null; then
        dnf install -y \
            python3 \
            python3-pip \
            python3-scikit-learn \
            python3-numpy \
            python3-joblib \
            wireless-tools \
            iw \
            wpa_supplicant \
            libpcap-devel \
            libnl3-devel \
            gcc \
            make \
            git \
            curl \
            sudo \
            procps-ng \
            aircrack-ng
    else
        yum install -y \
            python3 \
            python3-pip \
            wireless-tools \
            iw \
            wpa_supplicant \
            libpcap-devel \
            libnl3-devel \
            gcc \
            make \
            git \
            curl \
            sudo \
            procps
    fi

    # Build reaver + pixiewps + bully from source on RHEL-family
    cd /tmp
    if ! command -v reaver &>/dev/null; then
        info "Building reaver from source..."
        git clone https://github.com/t6x/reaver-wps-fork-t6x.git
        cd reaver-wps-fork-t6x/src
        ./configure
        make -j"$(nproc)"
        make install
        cd /tmp
    fi

    if ! command -v pixiewps &>/dev/null; then
        info "Building pixiewps from source..."
        git clone https://github.com/wiire-a/pixiewps.git
        cd pixiewps
        make -j"$(nproc)"
        make install
        cd /tmp
    fi

    if ! command -v bully &>/dev/null; then
        info "Building bully from source..."
        git clone https://github.com/aanarchyy/bully.git
        cd bully/src
        make -j"$(nproc)"
        cp bully /usr/local/bin/
        cd /tmp
    fi

    rm -rf /tmp/reaver-wps-fork-t6x /tmp/pixiewps /tmp/bully
}

# ── Unknown Distro Warning ───────────────────────────────────
setup_unknown() {
    warn "Unsupported distro detected. Attempting Debian-style install..."
    warn "If this fails, please install the following manually:"
    warn "  python3, pip3, iw, reaver, pixiewps, bully, aircrack-ng, git, curl"
    warn ""

    # Try apt-based install as fallback
    if command -v apt-get &>/dev/null; then
        setup_debian
    elif command -v dnf &>/dev/null; then
        setup_fedora
    elif command -v pacman &>/dev/null; then
        setup_arch
    elif command -v apk &>/dev/null; then
        setup_alpine
    else
        err "No supported package manager found. Install dependencies manually."
    fi
}

# ── Install Python dependencies ──────────────────────────────
install_python_deps() {
    info "Installing Python dependencies..."
    if command -v pip3 &>/dev/null; then
        pip3 install --break-system-packages scikit-learn numpy joblib 2>/dev/null || \
        pip3 install scikit-learn numpy joblib
    elif command -v pip &>/dev/null; then
        pip install scikit-learn numpy joblib
    fi
}

# ── Install wifi4 command ────────────────────────────────────
install_wifi4() {
    info "Installing wifi4 command..."

    # Create the wrapper script
    cat > "$WIFI4_BIN" << WIFIEOF
#!/bin/bash
# OPXoneshot (wifi4) launcher
# Installed by install.sh
exec python3 "${SCRIPT_DIR}/oneshot.py" "\$@"
WIFIEOF

    chmod +x "$WIFI4_BIN"
    chmod +x "$SCRIPT_DIR/oneshot.py" 2>/dev/null || true
    ok "wifi4 command installed to ${WIFI4_BIN}"
}

# ── Verify Installation ──────────────────────────────────────
verify_install() {
    info "Verifying installation..."

    local PASS=0
    local FAIL=0

    # Check required commands
    for cmd in python3 iw curl git; do
        if command -v "$cmd" &>/dev/null; then
            ok "  $cmd: $(command -v "$cmd")"
            PASS=$((PASS + 1))
        else
            warn "  $cmd: NOT FOUND"
            FAIL=$((FAIL + 1))
        fi
    done

    # Check Python packages
    if python3 -c "import sklearn; import numpy; import joblib" 2>/dev/null; then
        ok "  Python packages (sklearn, numpy, joblib): OK"
        PASS=$((PASS + 1))
    else
        warn "  Python packages: Some missing"
        FAIL=$((FAIL + 1))
    fi

    # Check pentest tools
    for tool in reaver pixiewps; do
        if command -v "$tool" &>/dev/null; then
            ok "  $tool: $(command -v "$tool")"
            PASS=$((PASS + 1))
        else
            warn "  $tool: NOT FOUND (may still work without it)"
        fi
    done

    # Check wifi4
    if command -v wifi4 &>/dev/null; then
        ok "  wifi4: $(command -v wifi4)"
        PASS=$((PASS + 1))
    else
        warn "  wifi4: NOT FOUND in PATH"
        FAIL=$((FAIL + 1))
    fi

    echo ""
    ok "Verification: ${PASS} passed, ${FAIL} warnings"
}

# ── Main ─────────────────────────────────────────────────────
main() {
    echo ""
    echo -e "${CYAN}╔══════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║     OPXoneshot (wifi4) — Universal Installer    ║${NC}"
    echo -e "${CYAN}║     AI-Powered WPS Vulnerability Platform       ║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════╝${NC}"
    echo ""

    detect_distro

    case "$DISTRO" in
        alpine)  setup_alpine ;;
        kali|debian|ubuntu|parrot) setup_debian ;;
        arch)    setup_arch ;;
        fedora|centos) setup_fedora ;;
        *)       setup_unknown ;;
    esac

    install_python_deps
    install_wifi4
    verify_install

    echo ""
    ok "═══════════════════════════════════════════════════"
    ok "Installation complete!"
    ok ""
    ok "Run from anywhere: wifi4"
    ok "Or directly:       python3 ${SCRIPT_DIR}/oneshot.py --ai"
    ok "═══════════════════════════════════════════════════"
    echo ""
}

main "$@"
