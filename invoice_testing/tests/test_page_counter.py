import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from invoice_testing.scripts.page_counter import counting_page
def test_method1():
    expected = {'invoice_1.pdf': {'pages': 3, 'credits': 3}, 
                'invoice_2.pdf': {'pages': 1, 'credits': 1}, 
                'invoice_3.pdf': {'pages': 1, 'credits': 1}, 
                'invoice_4.pdf': {'pages': 2, 'credits': 2}, 
                'invoice_5.pdf': {'pages': 2, 'credits': 2}}
    invoices_path = Path("invoice_testing/invoices")
    assert expected == counting_page(invoices_path)
def test_method2():
    invoices_path = Path("invoice_testing/expected")
    expected = {}
    assert expected == counting_page(invoices_path)
    