#!/bin/bash

# CRDB Fee Calculator Installation Script
# Dieses Skript installiert das crdbfee Tool auf Linux-Systemen

set -e

echo "🚀 CRDB Fee Calculator Installation wird gestartet..."

# Prüfe ob Python 3 installiert ist
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 ist nicht installiert. Bitte installieren Sie Python 3 zuerst."
    exit 1
fi

# Prüfe Python Version (mindestens 3.7)
PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 7 ]); then
    echo "❌ Python 3.7 oder höher ist erforderlich. Gefunden: $PYTHON_VERSION"
    exit 1
fi

echo "✅ Python $PYTHON_VERSION gefunden"

# Prüfe ob pip installiert ist
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 ist nicht installiert. Bitte installieren Sie pip3 zuerst."
    exit 1
fi

echo "✅ pip3 gefunden"

# Installiere Abhängigkeiten
echo "📦 Installiere Python-Abhängigkeiten..."
pip3 install -r requirements.txt

# Erstelle Installationsverzeichnis
INSTALL_DIR="/usr/local/bin"
echo "📁 Installiere in $INSTALL_DIR..."

# Kopiere das Skript
sudo cp crdbfee.py "$INSTALL_DIR/crdbfee"

# Mache es ausführbar
sudo chmod +x "$INSTALL_DIR/crdbfee"

# Prüfe ob die Installation erfolgreich war
if [ -f "$INSTALL_DIR/crdbfee" ]; then
    echo "✅ Installation erfolgreich!"
    echo ""
    echo "🎉 Das crdbfee Tool wurde erfolgreich installiert!"
    echo ""
    echo "Verwendung:"
    echo "  crdbfee statement.xlsx"
    echo "  crdbfee --help"
    echo ""
    echo "Das Tool ist jetzt von überall verfügbar."
else
    echo "❌ Installation fehlgeschlagen!"
    exit 1
fi

