from assignments import add_assignment, complete_assignment, delete_assignment
from deadlines import get_due_today, is_valid_deadline
from display import display_assignments, display_summary
from filters import filter_by_subject, filter_unfinished
from reports import build_summary
from storage import save_assignments


def ask_id():
    text = input("Numer zadania: ").strip()
    if text.isdecimal():
        return int(text)
    print("Podaj numer zadania, np. 1.")
    return None


def persist(assignments):
    try:
        save_assignments(assignments)
    except OSError as error:
        print(f"Nie udało się zapisać zmian: {error}")
        print("Zmiany są w pamięci. Wybierz 9, aby ponowić zapis.")


def run_menu(assignments):
    while True:
        print("\n--- PLANER PRAC DOMOWYCH ---")
        print("1. Wszystkie zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz jako wykonane")
        print("4. Filtruj po przedmiocie")
        print("5. Zadania na dzisiaj")
        print("6. Zadania niewykonane")
        print("7. Usuń zadanie")
        print("8. Statystyki")
        print("9. Zapisz")
        print("0. Wyjdź")
        choice = input("Wybierz opcję: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            display_assignments(assignments)
        elif choice == "2":
            title = input("Tytuł: ").strip()
            subject = input("Przedmiot: ").strip()
            deadline = input("Termin (RRRR-MM-DD): ").strip()
            if not is_valid_deadline(deadline):
                print("Podaj poprawną datę, np. 2026-11-05.")
                continue
            print(add_assignment(assignments, title, subject, deadline))
            persist(assignments)
        elif choice == "3":
            assignment_id = ask_id()
            if assignment_id is not None:
                print(complete_assignment(assignments, assignment_id))
                persist(assignments)
        elif choice == "4":
            subject = input("Przedmiot: ")
            display_assignments(filter_by_subject(assignments, subject))
        elif choice == "5":
            display_assignments(get_due_today(assignments))
        elif choice == "6":
            display_assignments(filter_unfinished(assignments))
        elif choice == "7":
            assignment_id = ask_id()
            if assignment_id is not None:
                print(delete_assignment(assignments, assignment_id))
                persist(assignments)
        elif choice == "8":
            display_summary(build_summary(assignments))
        elif choice == "9":
            persist(assignments)
        else:
            print("Wybierz numer z menu.")
