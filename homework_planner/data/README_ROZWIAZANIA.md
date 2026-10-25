# Planer prac domowych — rozwiązania TODO

Materiał dla nauczyciela: kompletne rozwiązania wszystkich dziewięciu TODO.
Każdy blok poniżej to pełna zawartość wskazanego pliku po uzupełnieniu.
Można nim zastąpić zawartość pliku podczas omawiania rozwiązania.
Pozostałe pliki projektu nie wymagają zmian.

## assignments.py — TODO 1–4

```python
def add_assignment(assignments, title, subject, deadline):
    """Dodaje zadanie i zwraca komunikat dla użytkownika."""
    title = title.strip()
    subject = subject.strip()

    # TODO 1: Odrzucamy puste dane, także tekst zawierający same spacje.
    if not title or not subject:
        return "Tytuł i przedmiot nie mogą być puste."

    next_id = max((item["id"] for item in assignments), default=0) + 1


def complete_assignment(assignments, assignment_id):
    """Oznacza znalezione zadanie jako wykonane."""
    # TODO 3: Szukamy zadania i sprawdzamy jego obecny stan.
    for assignment in assignments:
        if assignment["id"] == assignment_id:
            if assignment["completed"]:
                return "To zadanie jest już wykonane."

            assignment["completed"] = True
            return "Oznaczono zadanie jako wykonane."

    return "Nie znaleziono zadania."


def delete_assignment(assignments, assignment_id):
    """Usuwa zadanie o podanym identyfikatorze."""
    # TODO 4: Po usunięciu natychmiast kończymy funkcję.
    for assignment in assignments:
        if assignment["id"] == assignment_id:
            assignments.remove(assignment)
            return "Usunięto zadanie."

    return "Nie znaleziono zadania."
```

### Jak to działa?

- `not title` sprawdza, czy tekst jest pusty. `or` wystarczy, gdy brakuje choć jednego pola.
- `append()` dodaje nowy element do listy.
- `max(..., default=0) + 1` wybiera numer większy od największego obecnego numeru. Dla pustej listy daje 1.
- `==` porównuje wartości, a `=` przypisuje nową wartość.
- `return` kończy całą funkcję, także jeśli znajduje się wewnątrz pętli.
- Komunikat „Nie znaleziono zadania” znajduje się za pętlą. Zwracamy go dopiero po sprawdzeniu wszystkich elementów.
- Nie kontynuujemy przeglądania listy po `remove()`, ponieważ usunięcie przesuwa jej elementy.

Numer zadania jest unikalny w bieżącej liście. Po usunięciu zadania o największym numerze ten numer może zostać użyty ponownie.
Format daty sprawdza już menu przed wywołaniem `add_assignment()`.

## filters.py — TODO 5 i 6

```python
def filter_by_subject(assignments, subject):
    """Zwraca nową listę zadań z wybranego przedmiotu."""
    result = []
    subject = subject.strip().lower()

    # TODO 5: Zbieramy zadania z pasującego przedmiotu.
    for assignment in assignments:
        if assignment["subject"].strip().lower() == subject:
            result.append(assignment)

    return result


def filter_unfinished(assignments):
    """Zwraca nową listę niewykonanych zadań."""
    result = []

    # TODO 6: Zbieramy tylko niewykonane zadania.
    for assignment in assignments:
        if not assignment["completed"]:
            result.append(assignment)

    return result
```

### Jak to działa?

Najpierw tworzymy pustą listę wyników. Pętla sprawdza każde zadanie, a warunek decyduje, czy dodać je do wyniku.
`return result` jest za pętlą, dzięki czemu sprawdzimy wszystkie zadania.

`strip()` usuwa skrajne spacje, a `lower()` zmienia litery na małe.
Dlatego wpisy `Matematyka`, `MATEMATYKA` oraz ` matematyka ` dają ten sam wynik.
`not assignment["completed"]` oznacza, że zadanie nie zostało wykonane.

## deadlines.py — TODO 7 i 8

```python
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

    # TODO 7: Oba warunki muszą być spełnione jednocześnie.
    if deadline < today and not assignment["completed"]:
        return True

    return False


def get_due_today(assignments):
    """Zwraca niewykonane zadania z terminem na dzisiaj."""
    today = date.today().isoformat()
    result = []

    # TODO 8: Sprawdzamy termin i stan zadania.
    for assignment in assignments:
        if assignment["deadline"] == today and not assignment["completed"]:
            result.append(assignment)

    return result
```

### Jak to działa?

`date.fromisoformat()` zamienia tekst na datę, a `date.today()` pobiera dzisiejszą datę komputera.
Operator `<` sprawdza, czy termin jest wcześniejszy od dzisiaj.
`and` wymaga spełnienia obu warunków: termin minął i zadanie nadal jest niewykonane.

Zadanie z terminem dzisiaj nie jest zaległe. Wykonane zadanie nigdy nie jest zaległe.
W `get_due_today()` porównujemy dwa teksty w jednakowym formacie RRRR-MM-DD.

## reports.py — TODO 9

```python
from deadlines import is_overdue


def build_summary(assignments):
    completed = 0
    overdue = 0

    # TODO 9: Liczymy wykonane i zaległe zadania.
    for assignment in assignments:
        if assignment["completed"]:
            completed += 1

        if is_overdue(assignment):
            overdue += 1

    return {
        "total": len(assignments),
        "completed": completed,
        "unfinished": len(assignments) - completed,
        "overdue": overdue,
    }
```

### Jak to działa?

Liczniki zaczynają od zera. `completed += 1` to skrót zapisu `completed = completed + 1`.
Funkcja korzysta z `is_overdue()`, dzięki czemu regułę zaległości zapisujemy w jednym miejscu.
Zadania zaległe są częścią zadań niewykonanych, więc nie dodajemy tych dwóch liczb, aby otrzymać liczbę wszystkich zadań.

## Sprawdzenie po uzupełnieniu

Uruchom `python main.py` w folderze projektu. Na oryginalnych danych:

1. Filtr ` MATEMATYKA ` pokazuje zadania 1 i 4.
2. Lista niewykonanych pokazuje zadania 1, 2 i 4.
3. Statystyki pokazują 4 zadania, 1 wykonane i 3 niewykonane.
4. Dodanie zadania z pustym tytułem albo przedmiotem nie zmienia listy.
5. Pierwsze dodane zadanie dostaje numer 5.
6. Ukończenie zadania 1 usuwa je z listy niewykonanych.
7. Ponowne ukończenie zadania 1 wyświetla informację, że jest już wykonane.
8. Usunięcie zadania usuwa tylko wskazany element.
9. Operacje dla numeru 999 zwracają komunikat o braku zadania.
10. Ponowne uruchomienie programu odczytuje zapisane zmiany.

Aby sprawdzić terminy, dodaj trzy niewykonane zadania: z datą wczorajszą, dzisiejszą i jutrzejszą.
Tylko pierwsze powinno być zaległe, a tylko drugie powinno trafić na listę na dzisiaj.
Po ukończeniu pierwszego nie powinno już być zaległe.

## Pytania do uczniów

- Co się stanie, jeśli `return result` umieścimy wewnątrz pętli?
- Dlaczego do sprawdzenia zaległości używamy `and`, a do sprawdzenia pustych pól `or`?
- Dlaczego `len(assignments) + 1` może dać powtarzający się numer po usunięciu zadania?
- Dlaczego komunikat o braku zadania powinien znajdować się za pętlą?
