from PyPDF2 import PdfReader
from pathlib import Path
invoices_path = Path("invoice_testing/invoices")
results ={}
try:   
    for invoice in invoices_path.iterdir():
        try:
            if  invoice.is_file() and invoice.suffix == ".pdf":
                with invoice.open("rb") as file:
                    reader = PdfReader(file)
                    page_count = len(reader.pages)
                    credits = page_count
                    results[invoice.name] = {
                                              "pages": page_count,
                                              "credits": credits
                                            }
        except IOError:
            print("File can't be opened: invoice_name")
       
    print(results)        
            
except FileNotFoundError:
    print("Invalid Folder")        
    
        

            
    
    
    
    
