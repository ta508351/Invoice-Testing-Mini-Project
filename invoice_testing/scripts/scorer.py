"""expected= {
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
  "tax": 7240,
  "total": 45353.00
} """
from pathlib import Path
import json
def evaluating_accuracy(expected, extracted):
    result = {}
    total_fields = len(expected)
    mismatched_fields = []
    matched_fields = 0
    for key in expected:
        if key in extracted:
            if expected[key] == extracted[key]:
                matched_fields += 1
            else:
                mismatched_fields.append(key)
        else:
            mismatched_fields.append(key)

    score = matched_fields / total_fields
    result["score"] = score
    result["mismatched_fields"] = mismatched_fields
    return result


if __name__ == "__main__":
    expected_path = Path("invoice_testing/expected")
    extracted_path = Path("invoice_testing/extracted")

    results = []

    for expected_file in expected_path.iterdir():
        if expected_file.is_file() and expected_file.suffix == ".json":
            with expected_file.open("r", encoding="utf-8") as f:
                expected_data = json.load(f)

            invoice_name = expected_file.stem + ".pdf"
            extracted_file = extracted_path / expected_file.name
            if extracted_file.exists():
                try:
                    with extracted_file.open("r", encoding="utf-8") as f:
                        extracted_data = json.load(f)

                    score_result = evaluating_accuracy(expected_data, extracted_data)
                    result = {
                             "invoice": invoice_name,
                             "score": score_result["score"],
                            "mismatched_fields": score_result["mismatched_fields"]
                            }

                except json.JSONDecodeError:
                    
                    result = {
                        "invoice": invoice_name,
                        "score": 0,
                        "mismatched_fields": list(expected_data.keys())
                    }

           
            else:
                result = {
                    "invoice": invoice_name,
                    "score": 0,
                    "mismatched_fields": list(expected_data.keys())
                }

            results.append(result)


    for r in results:
        print(r)
