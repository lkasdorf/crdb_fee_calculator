#!/usr/bin/env python3
"""
CRDB Fee Calculator - Kommandozeilen-Tool zur Berechnung von Fees und VAT
aus Kontoauszügen im Excel-Format.
"""

import pandas as pd
import argparse
import sys
import os
from pathlib import Path
from typing import Optional, Tuple


class CRDBFeeCalculator:
    """Hauptklasse für die Berechnung von Fees und VAT aus CRDB Kontoauszügen."""
    
    FEE_KEYWORDS = "charge|commission|fee|levy|fund transfer"
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        
    def find_header_row(self, df: pd.DataFrame) -> int:
        """Findet die Zeile mit den Spaltenüberschriften."""
        for i, row in df.iterrows():
            if any(isinstance(cell, str) and "date" in cell.lower() for cell in row):
                return i
        return 0
    
    def parse_amount(self, val) -> Optional[float]:
        """Parst Beträge und entfernt Tausendertrennzeichen."""
        if pd.isna(val):
            return None
        val = str(val).strip()
        if val in ["", "nan", "None"]:
            return None
        # Tausendertrennzeichen entfernen
        val = val.replace(",", "")
        try:
            return float(val)
        except:
            return None
    
    def load_data(self) -> bool:
        """Lädt und bereitet die Excel-Datei vor."""
        try:
            # Datei laden
            df0 = pd.read_excel(self.file_path, dtype=str)
            header_idx = self.find_header_row(df0)
            
            self.df = pd.read_excel(self.file_path, skiprows=header_idx, dtype=str)
            
            # Erste Datenzeile als Kopf
            self.df.columns = self.df.iloc[0]
            self.df = self.df.drop(0).reset_index(drop=True)
            
            # Einheitliche Spaltennamen (wie bei CRDB-Exporten)
            self.df.columns = ["Posting Date", "Details", "Value Date", "Debit", "Credit", "Book Balance"]
            
            # Beträge parsen
            self.df["Debit"] = self.df["Debit"].apply(self.parse_amount)
            self.df["Credit"] = self.df["Credit"].apply(self.parse_amount)
            self.df["__details_lc"] = self.df["Details"].astype(str).str.lower()
            
            return True
            
        except Exception as e:
            print(f"Fehler beim Laden der Datei: {e}", file=sys.stderr)
            return False
    
    def calculate_fees_and_vat(self) -> Tuple[float, float]:
        """Berechnet die Gesamtbeträge für Fees und VAT."""
        if self.df is None:
            return 0.0, 0.0
        
        # VAT und Fees filtern
        vat_df = self.df[self.df["__details_lc"].str.contains("vat", na=False)]
        fees_df = self.df[
            self.df["__details_lc"].str.contains(self.FEE_KEYWORDS, na=False) & 
            ~self.df["__details_lc"].str.contains("vat", na=False)
        ]
        
        # Summen berechnen
        fees_total = fees_df["Debit"].sum(skipna=True) or 0.0
        vat_total = vat_df["Debit"].sum(skipna=True) or 0.0
        
        return fees_total, vat_total
    
    def print_results(self, fees_total: float, vat_total: float):
        """Gibt die Ergebnisse in einem schönen Format aus."""
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                    CRDB Fee Calculator                      ║")
        print("╠══════════════════════════════════════════════════════════════╣")
        print(f"║  📊  Fees/Charges: {fees_total:>15.2f} USD               ║")
        print(f"║  🏛️   VAT Total:    {vat_total:>15.2f} USD               ║")
        print("╚══════════════════════════════════════════════════════════════╝")


def main():
    """Hauptfunktion für das Kommandozeilen-Tool."""
    parser = argparse.ArgumentParser(
        description="CRDB Fee Calculator - Berechnet Fees und VAT aus Kontoauszügen",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  crdbfee statement.xlsx
  crdbfee /path/to/statement.xlsx
  crdbfee --help
        """
    )
    
    parser.add_argument(
        "file",
        help="Pfad zur Excel-Datei mit dem Kontoauszug"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="CRDB Fee Calculator v1.0.0"
    )
    
    args = parser.parse_args()
    
    # Prüfe ob Datei existiert
    if not os.path.exists(args.file):
        print(f"Fehler: Datei '{args.file}' existiert nicht.", file=sys.stderr)
        sys.exit(1)
    
    # Prüfe ob es eine Excel-Datei ist
    if not args.file.lower().endswith(('.xlsx', '.xls')):
        print(f"Fehler: Datei '{args.file}' ist keine Excel-Datei.", file=sys.stderr)
        sys.exit(1)
    
    # Berechne Fees und VAT
    calculator = CRDBFeeCalculator(args.file)
    
    if not calculator.load_data():
        sys.exit(1)
    
    fees_total, vat_total = calculator.calculate_fees_and_vat()
    calculator.print_results(fees_total, vat_total)


if __name__ == "__main__":
    main()

