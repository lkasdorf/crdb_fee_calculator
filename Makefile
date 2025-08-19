# CRDB Fee Calculator Makefile
# Verwendung: make install, make uninstall, make test

.PHONY: install uninstall test clean help

# Standardziel
all: help

# Installation
install:
	@echo "🚀 Installiere CRDB Fee Calculator..."
	@chmod +x install.sh
	@./install.sh

# Deinstallation
uninstall:
	@echo "🗑️  Deinstalliere CRDB Fee Calculator..."
	@chmod +x uninstall.sh
	@./uninstall.sh

# Test des Tools (falls eine Testdatei vorhanden ist)
test:
	@echo "🧪 Teste CRDB Fee Calculator..."
	@if [ -f "test_statement.xlsx" ]; then \
		echo "Teste mit test_statement.xlsx..."; \
		crdbfee test_statement.xlsx; \
	else \
		echo "Keine Testdatei gefunden. Erstellen Sie test_statement.xlsx für Tests."; \
	fi

# Aufräumen
clean:
	@echo "🧹 Räume auf..."
	@rm -f *.pyc
	@rm -rf __pycache__

# Hilfe anzeigen
help:
	@echo "CRDB Fee Calculator - Makefile"
	@echo ""
	@echo "Verfügbare Ziele:"
	@echo "  install    - Installiert das Tool"
	@echo "  uninstall  - Entfernt das Tool"
	@echo "  test       - Testet das Tool (falls Testdatei vorhanden)"
	@echo "  clean      - Räumt temporäre Dateien auf"
	@echo "  help       - Zeigt diese Hilfe an"
	@echo ""
	@echo "Beispiele:"
	@echo "  make install"
	@echo "  make test"
	@echo "  make uninstall"

