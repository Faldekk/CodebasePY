def add_assignment(assignments, title, subject, deadline):
    """Dodaje zadanie i zwraca komunikat dla użytkownika."""
    # TODO 1: Jeśli tytuł lub przedmiot jest pusty, zwróć komunikat o błędzie.
    # Wskazówka: metoda strip() usuwa spacje z początku i końca tekstu.

    next_id = max((item["id"] for item in assignments), default=0) + 1

    assignment = {
        "id": next_id,
        "title": title,
        "subject": subject,
        "deadline": deadline,
        "completed": False,
    }
    assignments.append(assignment)
    return "Dodano zadanie."


def complete_assignment(assignments, assignment_id):
    """Oznacza znalezione zadanie jako wykonane."""
    # TODO 3: Przejdź pętlą po zadaniach i porównaj ich id z assignment_id.
    # Jeśli znalezione zadanie jest już wykonane, zwróć odpowiedni komunikat.
    # W przeciwnym razie ustaw completed na True i zwróć komunikat o sukcesie.
    return "Nie znaleziono zadania."


def delete_assignment(assignments, assignment_id):
    """Usuwa zadanie o podanym identyfikatorze."""
    # TODO 4: Użyj pętli, aby znaleźć zadanie o podanym id.
    # Usuń je metodą remove() i od razu zakończ funkcję przez return.
    # Nie kontynuuj pętli po usunięciu elementu z listy.
    return "Nie znaleziono zadania."
