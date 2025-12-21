expected= {
  "vendor_name": "CPB Software (Germany) GmbH",
  "invoice_date": "2024.03.01",
  "invoice_number": "123100401",
  "currency": "EURO",
  "subtotal": 38112.00,
  "tax": 7241.00,
  "total": 45353.00}
extracted = {
  "vendor_name": "CPB Software (Germany) GmbH",
  "invoice_date": "2024.03.01",
  "invoice_number": "123100401",
  "currency": "EUR",
  "subtotal": 38112.00,
  "tax": 7240,
  "total": 45353.00
} 
def evaluating_accuracy(expected, extracted):
    result={}
    total_fields = len(expected)
    mismatched_fields= []
    matched_fields = 0
    for key, value in expected.items():
      if key  in extracted:
        if expected[key] == extracted[key]:
          matched_fields+=1
        else:
          mismatched_fields.append(key)
      else:
        mismatched_fields.append(key)
    score = matched_fields / total_fields
    result["invoice"] = "invoice_1.pdf"
    result["score"]= score
    result["mismatched_fields"]= mismatched_fields
    return result
if __name__ == "__main__":
  result = evaluating_accuracy(expected,extracted)
  print(result)
      
          
    
   
    
    
    
    