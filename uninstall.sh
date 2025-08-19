#!/bin/bash

# CRDB Fee Calculator Deinstallation Script

echo "🗑️  CRDB Fee Calculator Deinstallation wird gestartet..."

INSTALL_DIR="/usr/local/bin"
TOOL_NAME="crdbfee"

# Prüfe ob das Tool installiert ist
if [ -f "$INSTALL_DIR/$TOOL_NAME" ]; then
    echo "📁 Entferne $TOOL_NAME aus $INSTALL_DIR..."
    sudo rm "$INSTALL_DIR/$TOOL_NAME"
    
    if [ ! -f "$INSTALL_DIR/$TOOL_NAME" ]; then
        echo "✅ Deinstallation erfolgreich!"
        echo "Das crdbfee Tool wurde erfolgreich entfernt."
    else
        echo "❌ Deinstallation fehlgeschlagen!"
        exit 1
    fi
else
    echo "ℹ️  Das Tool ist nicht installiert."
fi

echo ""
echo "Hinweis: Python-Pakete wurden nicht entfernt."
echo "Falls Sie diese auch entfernen möchten, führen Sie aus:"
echo "  pip3 uninstall pandas openpyxl xlrd"

