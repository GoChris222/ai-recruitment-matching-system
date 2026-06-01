import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_json(filename: str):
    file_path = DATA_DIR / filename

    if not file_path.exists():
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(filename: str, data):
    file_path = DATA_DIR / filename

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
