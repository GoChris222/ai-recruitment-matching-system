import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_json(filename):
    filepath = DATA_DIR / filename

    with open(filepath, "r") as file:
        return json.load(file)


def save_json(filename, data):
    filepath = DATA_DIR / filename

    with open(filepath, "w") as file:
        json.dump(data, file, indent=2)
