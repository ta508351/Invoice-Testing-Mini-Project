import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from invoice_testing.scripts.scorer import evaluating_accuracy
def test_method1():
    expected_data={
  "vendor_name": "CPB Software (Germany) GmbH",
  "invoice_date": "2024.03.01",
  "invoice_number": "123100401",
  "currency": "EURO",
  "subtotal": 38112.00,
  "tax": 7241.00,
  "total": 45353.00}
    extracted_data = {
  "vendor_name": "CPB Software (Germany) GmbH",
  "invoice_date": "2024.03.01",
  "invoice_number": "123100401",
  "currency": "EUR",
  "tax": 7240,
  "total": 45353.00
} 
    result = {
                        "score": 0.5714285714285714,
                        "mismatched_fields": ['currency',  'subtotal' ,'tax']
                    }
    assert result == evaluating_accuracy(expected_data, extracted_data)
def test_method2():
    expected_data={
  "vendor_name": "DEMO - Sliced Invoices",
  "invoice_date": "2016.01.25",
  "invoice_number": "INV-3337",
  "currency": "USD",
  "subtotal": 85.00,
  "tax": 8.50,
  "total": 93.50
}
    extracted_data="Tanya Agrawal"
    result={
             "score": 0,
             "mismatched_fields": []
    }
    assert result==evaluating_accuracy(expected_data, extracted_data)

        