from PyPDF2 import PdfReader
from pathlib import Path
invoices_path = Path("invoice_testing/invoices")
def counting_page():
    result ={}
    try:   
        for invoice in invoices_path.iterdir():
            try:
                if  invoice.is_file() and invoice.suffix == ".pdf":
                    with invoice.open("rb") as file:
                        reader = PdfReader(file)
                        page_count = len(reader.pages)
                        credits = page_count
                        result[invoice.name] = {
                                              "pages": page_count,
                                              "credits": credits
                                            }
                    
            except IOError:
                print("File can't be opened: invoice_name")
    except FileNotFoundError:
        print("Invalid Folder") 
    return result  
if __name__ == "__main__":
    result = counting_page()
    print(result)         
    
        

            
    
    
    
    
