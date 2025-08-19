#!/usr/bin/env python3
"""
Erstellt eine Test-Excel-Datei für den CRDB Fee Calculator
"""

import pandas as pd
import numpy as np

def create_test_statement():
    """Erstellt eine Test-Kontoauszug-Datei."""
    
    # Beispieldaten
    data = {
        'Posting Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05'],
        'Details': [
            'Bank Transfer Fee',
            'VAT on Commission',
            'Account Maintenance Charge',
            'Wire Transfer Fee',
            'VAT on Bank Charges'
        ],
        'Value Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05'],
        'Debit': [25.00, 5.00, 15.00, 30.00, 6.00],
        'Credit': [0, 0, 0, 0, 0],
        'Book Balance': [1000.00, 995.00, 980.00, 950.00, 944.00]
    }
    
    # DataFrame erstellen
    df = pd.DataFrame(data)
    
    # In Excel-Datei speichern
    filename = 'test_statement.xlsx'
    df.to_excel(filename, index=False)
    
    print(f"✅ Testdatei '{filename}' wurde erstellt!")
    print(f"📊 Enthält {len(data['Posting Date'])} Transaktionen")
    print(f"💰 Erwartete Fees: {sum(data['Debit'][::2])} (ohne VAT)")
    print(f"🏛️  Erwarteter VAT: {sum(data['Debit'][1::2])}")
    print(f"")
    print(f"Sie können das Tool jetzt testen mit:")
    print(f"  crdbfee {filename}")

if __name__ == "__main__":
    create_test_statement()

