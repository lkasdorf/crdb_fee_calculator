# CRDB Fee Calculator

Ein Kommandozeilen-Tool zur Berechnung von Fees und VAT aus CRDB Kontoauszügen im Excel-Format.

## Features

- 🚀 Einfache Kommandozeilen-Bedienung
- 📊 Automatische Erkennung von Fees/Charges
- 🏛️ VAT-Berechnung
- 💱 **Automatische Währungserkennung (USD/TZS)**
- 💰 Unterstützung für verschiedene Währungen
- 🎨 Schöne, formatierte Ausgabe
- 📁 Unterstützt .xlsx und .xls Dateien

## Installation

### Voraussetzungen

- Linux-System
- Python 3.7 oder höher
- pip3

### Schnellinstallation

1. Repository klonen oder herunterladen
2. Installationsskript ausführbar machen:
   ```bash
   chmod +x install.sh
   ```
3. Installation ausführen:
   ```bash
   ./install.sh
   ```

Das Tool wird automatisch in `/usr/local/bin` installiert und ist damit von überall verfügbar.

### Manuelle Installation

1. Abhängigkeiten installieren:
   ```bash
   pip3 install -r requirements.txt
   ```

2. Skript ausführbar machen und in PATH kopieren:
   ```bash
   chmod +x crdbfee.py
   sudo cp crdbfee.py /usr/local/bin/crdbfee
   ```

## Verwendung

### Grundlegende Verwendung

```bash
crdbfee statement.xlsx
```

### Hilfe anzeigen

```bash
crdbfee --help
```

### Version anzeigen

```bash
crdbfee --version
```

## Beispielausgabe

### USD Ausgabe
```
╔══════════════════════════════════════════════════════════════╗
║                    CRDB Fee Calculator                      ║
╠══════════════════════════════════════════════════════════════╣
║  📊  Fees/Charges:          125.50 USD                    ║
║  🏛️   VAT Total:             25.10 USD                    ║
╚══════════════════════════════════════════════════════════════╝
💱 Erkannte Währung: USD
```

### TZS Ausgabe
```
╔══════════════════════════════════════════════════════════════╗
║                    CRDB Fee Calculator                      ║
╠══════════════════════════════════════════════════════════════╣
║  📊  Fees/Charges:        25000.00 TZS                    ║
║  🏛️   VAT Total:           5000.00 TZS                    ║
╚══════════════════════════════════════════════════════════════╝
💱 Erkannte Währung: TZS
```

## Deinstallation

```bash
chmod +x uninstall.sh
./uninstall.sh
```

## Unterstützte Dateiformate

- Excel (.xlsx)
- Excel (.xls)

## Erkennung von Fees und VAT

Das Tool erkennt automatisch:

**Fees/Charges:**
- charge
- commission
- fee
- levy
- fund transfer

**VAT:**
- Alle Einträge mit "vat" im Beschreibungstext

## Währungserkennung

Das Tool erkennt automatisch die Währung aus:
- Spaltennamen (z.B. "Balance USD", "Amount TZS")
- Beschreibungstexten (z.B. "Bank Fee USD", "Commission TZS")
- Währungssymbolen ($, TSH, TZS)
- Fallback: USD (Standard)

**Unterstützte Währungen:**
- **USD**: US Dollar
- **TZS**: Tanzania Shilling

## Fehlerbehebung

### "Datei existiert nicht"
- Überprüfen Sie den Dateipfad
- Stellen Sie sicher, dass die Datei im aktuellen Verzeichnis liegt

### "Keine Excel-Datei"
- Verwenden Sie nur .xlsx oder .xls Dateien
- Stellen Sie sicher, dass die Datei nicht beschädigt ist

### "Python nicht gefunden"
- Installieren Sie Python 3.7 oder höher
- Stellen Sie sicher, dass `python3` im PATH verfügbar ist

## Lizenz

Siehe [LICENSE](LICENSE) Datei für Details.

## Support

Bei Problemen oder Fragen erstellen Sie bitte ein Issue im Repository.
