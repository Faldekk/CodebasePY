from deadlines import is_overdue


def display_assignments(assignments):
    if not assignments:
        print("Brak zadań do wyświetlenia.")
        return

    for assignment in assignments:
        status = "DO ZROBIENIA"
        if assignment["completed"]:
            status = "WYKONANE"
        elif is_overdue(assignment):
            status = "ZALEGŁE"

        print(
            f"#{assignment['id']} | {assignment['title']}\n"
            f"  Przedmiot: {assignment['subject']} | "
            f"Termin: {assignment['deadline']} | {status}"
        )


def display_summary(summary):
    print(f"Wszystkie: {summary['total']}")
    print(f"Wykonane: {summary['completed']}")
    print(f"Do zrobienia: {summary['unfinished']}")
    print(f"Zaległe: {summary['overdue']}")
