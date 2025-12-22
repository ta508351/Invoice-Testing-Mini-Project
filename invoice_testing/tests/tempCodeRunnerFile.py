import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from invoice_testing.scripts.scorer import evaluating_accuracy
