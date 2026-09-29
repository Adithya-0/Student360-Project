import json
from pathlib import Path


def load_json(filename, default=None):
    path = Path(filename)
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return default if default is not None else []


def save_json(filename, data):
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
