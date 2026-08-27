#!/bin/bash
# wifi4 — Global installer for OneShot AI
# Run this ONCE to install wifi4 command system-wide
# Usage: sudo bash install_wifi4.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
INSTALL_DIR="/usr/local/bin"
ONESHOT_DIR="$INSTALL_DIR/oneshot-ai"

echo "[*] Installing OneShot AI globally..."

# Create install directory
mkdir -p "$ONESHOT_DIR"

# Copy files
cp "$SCRIPT_DIR/oneshot.py" "$ONESHOT_DIR/"
cp -r "$SCRIPT_DIR/models" "$ONESHOT_DIR/" 2>/dev/null || true
cp "$SCRIPT_DIR/vulnwsc.txt" "$ONESHOT_DIR/" 2>/dev/null || true
chmod +x "$ONESHOT_DIR/oneshot.py"

# Create global wifi4 command
cat > "$INSTALL_DIR/wifi4" << 'WIFI4_EOF'
#!/bin/bash
# wifi4 — OneShot AI autonomous WiFi tool
# Works from ANY directory
exec python3 /usr/local/bin/oneshot-ai/oneshot.py --ai "$@"
WIFI4_EOF
chmod +x "$INSTALL_DIR/wifi4"

# Create global oneshot command
cat > "$INSTALL_DIR/oneshot" << 'ONESHOT_EOF'
#!/bin/bash
# oneshot — OneShot AI WiFi tool
# Works from ANY directory
exec python3 /usr/local/bin/oneshot-ai/oneshot.py "$@"
ONESHOT_EOF
chmod +x "$INSTALL_DIR/oneshot"

echo "[+] Installed!"
echo "[+] Usage: wifi4"
echo "[+] Usage: oneshot --ai"
echo "[+] Usage: oneshot --check BSSID"
echo "[+] Location: $ONESHOT_DIR/"
