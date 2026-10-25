from datetime import date


def is_valid_deadline(text):
    """Sprawdza datę wpisaną przez użytkownika."""
    try:
        parsed = date.fromisoformat(text)
        return parsed.isoformat() == text
    except ValueError:
        return False


def is_overdue(assignment):
    """Zadanie jest zaległe, jeśli termin minął i nie zostało wykonane."""
    deadline = date.fromisoformat(assignment["deadline"])
    today = date.today()
    # TODO 7: Jeśli deadline jest wcześniejszy niż today ORAZ zadanie
    # nie jest wykonane, zwróć True. W pozostałych przypadkach zwróć False.
    return False


def get_due_today(assignments):
    """Zwraca niewykonane zadania z terminem na dzisiaj."""
    today = date.today().isoformat()
    result = []
    # TODO 8: Przejdź pętlą po zadaniach. Dodaj do result te, których
    # deadline jest równy today i completed jest równe False.
    return result
