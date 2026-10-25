"""Proste okno planera. Uruchom: python gui.py."""
import tkinter as tk
from datetime import date
from tkinter import messagebox, ttk

from assignments import add_assignment, complete_assignment, delete_assignment
from deadlines import get_due_today, is_overdue, is_valid_deadline
from filters import filter_by_subject, filter_unfinished
from storage import load_assignments, save_assignments


def main():
    root = tk.Tk()
    root.title("Mój planer prac domowych")
    root.geometry("850x560")
    root.minsize(700, 500)

    try:
        assignments = load_assignments()
    except (OSError, ValueError) as error:
        messagebox.showerror("Nie można wczytać danych", str(error), parent=root)
        root.destroy()
        return

    # StringVar łączy pole formularza ze zmienną w Pythonie.
    title = tk.StringVar()
    subject = tk.StringVar()
    deadline = tk.StringVar(value=date.today().isoformat())
    subject_filter = tk.StringVar()
    view = tk.StringVar(value="Wszystkie")
    status = tk.StringVar(value="Wybierz zadanie z listy lub dodaj nowe.")

    page = ttk.Frame(root, padding=16)
    page.pack(fill="both", expand=True)
    ttk.Label(page, text="Mój planer prac domowych", font=("Segoe UI", 18, "bold")).pack(anchor="w")
    ttk.Label(page, text="Małymi krokami do odrobionych lekcji.").pack(anchor="w", pady=(0, 12))

    form = ttk.LabelFrame(page, text="Nowe zadanie", padding=10)
    form.pack(fill="x")
    for column, (label, variable) in enumerate([
        ("Co trzeba zrobić?", title),
        ("Przedmiot", subject),
        ("Termin (RRRR-MM-DD)", deadline),
    ]):
        ttk.Label(form, text=label).grid(row=0, column=column, sticky="w")
        ttk.Entry(form, textvariable=variable).grid(row=1, column=column, sticky="ew", padx=(0, 8))
        form.columnconfigure(column, weight=1)

    toolbar = ttk.Frame(page)
    toolbar.pack(fill="x", pady=12)
    ttk.Label(toolbar, text="Widok:").pack(side="left")
    chooser = ttk.Combobox(toolbar, textvariable=view, state="readonly", width=16,
                           values=["Wszystkie", "Niewykonane", "Na dzisiaj", "Przedmiot"])
    chooser.pack(side="left", padx=6)
    ttk.Entry(toolbar, textvariable=subject_filter, width=18).pack(side="left")

    table = ttk.Treeview(page, columns=("title", "subject", "deadline", "status"), show="headings", selectmode="browse")
    for name, label, width in [
        ("title", "Zadanie", 290), ("subject", "Przedmiot", 130),
        ("deadline", "Termin", 110), ("status", "Stan", 120),
    ]:
        table.heading(name, text=label)
        table.column(name, width=width, minwidth=80)
    table.tag_configure("overdue", foreground="#b42318")
    table.tag_configure("completed", foreground="#28744c")
    table.pack(fill="both", expand=True)

    # Odświeżanie korzysta z tych samych funkcji, co menu terminalowe.
    def refresh():
        items = assignments
        if view.get() == "Niewykonane":
            items = filter_unfinished(assignments)
        elif view.get() == "Na dzisiaj":
            items = get_due_today(assignments)
        elif view.get() == "Przedmiot":
            items = filter_by_subject(assignments, subject_filter.get())

        for row in table.get_children():
            table.delete(row)
        for item in items:
            label, tag = "Do zrobienia", "unfinished"
            if item["completed"]:
                label, tag = "Wykonane", "completed"
            elif is_overdue(item):
                label, tag = "Zaległe", "overdue"
            table.insert("", "end", iid=str(item["id"]), values=(
                item["title"], item["subject"], item["deadline"], label,
            ), tags=(tag,))

    def save():
        try:
            save_assignments(assignments)
        except OSError as error:
            status.set("Zapis nieudany. Zmiany są w pamięci — ponów zapis.")
            messagebox.showerror("Błąd zapisu", str(error), parent=root)
            return False
        return True

    def add():
        if not is_valid_deadline(deadline.get().strip()):
            messagebox.showwarning("Niepoprawna data", "Podaj datę w formacie RRRR-MM-DD.", parent=root)
            return
        count_before = len(assignments)
        result = add_assignment(assignments, title.get(), subject.get(), deadline.get().strip())
        status.set(result)
        if len(assignments) > count_before:
            title.set("")
            save()
        refresh()

    def change_selected(action):
        selected = table.selection()
        if not selected:
            messagebox.showinfo("Wybierz zadanie", "Kliknij najpierw zadanie na liście.", parent=root)
            return
        if action == "delete":
            if not messagebox.askyesno("Usuwanie", "Usunąć wybrane zadanie?", parent=root):
                return
            result = delete_assignment(assignments, int(selected[0]))
        else:
            result = complete_assignment(assignments, int(selected[0]))
        status.set(result)
        save()
        refresh()

    def save_manually():
        if save():
            status.set("Zapisano zadania.")

    def close():
        if save():
            root.destroy()

    ttk.Button(form, text="Dodaj", command=add).grid(row=1, column=3)
    ttk.Button(toolbar, text="Pokaż", command=refresh).pack(side="left", padx=6)
    chooser.bind("<<ComboboxSelected>>", lambda event: refresh())

    actions = ttk.Frame(page)
    actions.pack(fill="x", pady=10)
    ttk.Button(actions, text="Oznacz jako wykonane", command=lambda: change_selected("complete")).pack(side="left")
    ttk.Button(actions, text="Usuń", command=lambda: change_selected("delete")).pack(side="left", padx=6)
    ttk.Button(actions, text="Zapisz", command=save_manually).pack(side="right")
    ttk.Label(page, textvariable=status, wraplength=650).pack(anchor="w")
    ttk.Label(page, text="Funkcje aplikacji zaczną działać po uzupełnieniu odpowiednich TODO.", wraplength=650).pack(anchor="w", pady=(6, 0))

    root.protocol("WM_DELETE_WINDOW", close)
    refresh()
    root.mainloop()


if __name__ == "__main__":
    main()
