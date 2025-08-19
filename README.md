# CRDB Fee Calculator

A command line tool for calculating fees and VAT from CRDB account statements in Excel format.

## Features

- 🚀 Simple command line interface
- 📊 Automatic detection of fees/charges
- 🏛️ VAT calculation
- 💱 **Automatic currency detection (USD/TZS)**
- 💰 Support for different currencies
- 🎨 Beautiful, formatted output
- 📁 Supports .xlsx and .xls files

## Installation

### Requirements

- Linux system
- Python 3.7 or higher
- pip3

### Quick Installation

1. Clone or download repository
2. Make installation script executable:
   ```bash
   chmod +x install.sh
   ```
3. Run installation:
   ```bash
   ./install.sh
   ```

The tool will be automatically installed in `/usr/local/bin` and will be available from anywhere.

### Manual Installation

1. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

2. Make script executable and copy to PATH:
   ```bash
   chmod +x crdbfee.py
   sudo cp crdbfee.py /usr/local/bin/crdbfee
   ```

## Usage

### Basic Usage

```bash
crdbfee statement.xlsx
```

### Show Help

```bash
crdbfee --help
```

### Show Version

```bash
crdbfee --version
```

## Example Output

### USD Output
```
╔══════════════════════════════════════════════════════════════╗
║                    CRDB Fee Calculator                      ║
╠══════════════════════════════════════════════════════════════╣
║  📊  Fees/Charges:          125.50 USD                     ║
║  🏛️   VAT Total:             25.10 USD                     ║
╠══════════════════════════════════════════════════════════════╣
║  💰  Total Amount:          150.60 USD                     ║
╚══════════════════════════════════════════════════════════════╝
💱 Detected currency: USD
```

### TZS Output
```
╔══════════════════════════════════════════════════════════════╗
║                    CRDB Fee Calculator                      ║
╠══════════════════════════════════════════════════════════════╣
║  📊  Fees/Charges:        25000.00 TZS                     ║
║  🏛️   VAT Total:           5000.00 TZS                     ║
╠══════════════════════════════════════════════════════════════╣
║  💰  Total Amount:        30000.00 TZS                     ║
╚══════════════════════════════════════════════════════════════╝
💱 Detected currency: TZS
```

## Uninstallation

```bash
chmod +x uninstall.sh
./uninstall.sh
```

## Supported File Formats

- Excel (.xlsx)
- Excel (.xls)

## Detection of Fees and VAT

The tool automatically detects:

**Fees/Charges:**
- charge
- commission
- fee
- levy
- fund transfer

**VAT:**
- All entries with "vat" in the description text

## Currency Detection

The tool automatically detects the currency from:
- Column names (e.g., "Balance USD", "Amount TZS")
- Description texts (e.g., "Bank Fee USD", "Commission TZS")
- Currency symbols ($, TSH, TZS)
- Fallback: USD (default)

**Supported Currencies:**
- **USD**: US Dollar
- **TZS**: Tanzania Shilling

## Troubleshooting

### "File does not exist"
- Check the file path
- Make sure the file is in the current directory

### "Not an Excel file"
- Use only .xlsx or .xls files
- Make sure the file is not corrupted

### "Python not found"
- Install Python 3.7 or higher
- Make sure `python3` is available in PATH

## License

See [LICENSE](LICENSE) file for details.

## Support

For problems or questions, please create an issue in the repository.
