from deadlines import is_overdue


def build_summary(assignments):
    completed = 0
    overdue = 0
    # TODO 9: Przejdź pętlą po zadaniach.
    # Zwiększ completed o 1, jeśli zadanie jest wykonane.
    # Zwiększ overdue o 1, jeśli is_overdue(zadanie) zwraca True.
    return {
        "total": len(assignments),
        "completed": completed,
        "unfinished": len(assignments) - completed,
        "overdue": overdue,
    }
