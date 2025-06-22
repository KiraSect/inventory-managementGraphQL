import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.json"

def read_data():
    if not DATA_FILE.exists():
        return {"products": [], "stock_changes": []}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def write_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
