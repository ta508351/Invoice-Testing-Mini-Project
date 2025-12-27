from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import os
invoices = []
invoices = [{"invoice_name" : "invoice_1.pdf",
        "pages" : 3,
        "credits_used" : 3,
        "accuracy_score" : 71.4,
        "error_count": 2
        },
        {"invoice_name" : "invoice_2.pdf",
        "pages" : 1,
        "credits_used" : 1,
        "accuracy_score" : 71.4,
        "error_count": 2
        },
        {"invoice_name" : "invoice_3.pdf",
        "pages" : 1,
        "credits_used" : 1,
        "accuracy_score" : 0,
        "error_count": 7
        },
        {"invoice_name" : "invoice_4.pdf",
        "pages" : 2,
        "credits_used" : 2,
        "accuracy_score" : 57.1,
        "error_count": 3
        },
        {"invoice_name" : "invoice_5.pdf",
        "pages" : 2,
        "credits_used" : 2,
        "accuracy_score" : 42.8,
        "error_count": 4
        },
        ]
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / "templates"

env = Environment(
    loader=FileSystemLoader(str(TEMPLATE_DIR))
)

template = env.get_template("report.html")

rendered_html = template.render(invoices=invoices)

os.makedirs("report", exist_ok=True)

with open("report/results.html", "w", encoding="utf-8") as f:
    f.write(rendered_html)

print("✅ Report generated successfully: report/results.html")
