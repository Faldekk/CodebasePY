import json
from pathlib import Path

from deadlines import is_valid_deadline

DATA_PATH = Path(__file__).resolve().parent / "data" / "homework.json"


def load_assignments():
    if not DATA_PATH.exists():
        return []
    with DATA_PATH.open("r", encoding="utf-8") as file:
        assignments = json.load(file)

    if not isinstance(assignments, list):
        raise ValueError("Plik danych musi zawierać listę zadań.")

    ids = set()
    for item in assignments:
        if not isinstance(item, dict):
            raise ValueError("Każde zadanie musi być słownikiem.")
        if type(item.get("id")) is not int or item["id"] <= 0:
            raise ValueError("Identyfikator musi być dodatnią liczbą całkowitą.")
        if item["id"] in ids:
            raise ValueError("Identyfikatory zadań nie mogą się powtarzać.")
        ids.add(item["id"])
        for key in ("title", "subject", "deadline"):
            if not isinstance(item.get(key), str):
                raise ValueError(f"Pole {key} musi zawierać tekst.")
        if not is_valid_deadline(item["deadline"]):
            raise ValueError("Niepoprawna data w pliku danych.")
        if type(item.get("completed")) is not bool:
            raise ValueError("Pole completed musi mieć wartość true lub false.")
    return assignments


def save_assignments(assignments):
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = DATA_PATH.with_suffix(".tmp")
    with temporary_path.open("w", encoding="utf-8") as file:
        json.dump(assignments, file, ensure_ascii=False, indent=2)
    temporary_path.replace(DATA_PATH)
