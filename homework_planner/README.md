# Planer prac domowych

Prosta aplikacja do zapisywania prac domowych i pilnowania terminów. Każde zadanie ma tytuł, przedmiot, termin wykonania oraz informację, czy zostało już ukończone.

## Uruchomienie

Aplikacja wymaga Pythona 3.10 lub nowszego. Otwórz terminal w folderze `homework_planner` i wpisz:

```sh
python gui.py
```

Otworzy się okno planera. Możesz również korzystać z wersji tekstowej:

```sh
python main.py
```

## Dodawanie zadania

Wypełnij pola „Co trzeba zrobić?”, „Przedmiot” oraz „Termin”, a następnie kliknij „Dodaj”. Datę wpisz w formacie `RRRR-MM-DD`, np. `2026-11-05`.

Przykładowe zadanie:

- Co trzeba zrobić? Rozwiązać zadania ze strony 42.
- Przedmiot: Matematyka.
- Termin: 2026-11-05.

## Przeglądanie zadań

Lista pokazuje tytuł, przedmiot, termin i stan każdego zadania. W polu „Widok” możesz wybrać:

- **Wszystkie** — całą listę zadań.
- **Niewykonane** — zadania, które nadal trzeba zrobić.
- **Na dzisiaj** — niewykonane zadania z dzisiejszym terminem.
- **Przedmiot** — zadania z wybranego przedmiotu. Wpisz jego nazwę w polu obok i kliknij „Pokaż”.

## Kończenie i usuwanie zadań

Kliknij zadanie na liście, a następnie wybierz „Oznacz jako wykonane” lub „Usuń”. Przed usunięciem aplikacja poprosi o potwierdzenie.

Zadania wykonane są wyświetlane na zielono. Zaległe zadania są czerwone. Zadanie jest zaległe, gdy jego termin minął i nie zostało jeszcze wykonane. Termin przypadający na dzisiaj nie oznacza zaległości.

## Zapis danych

Dane są przechowywane lokalnie w pliku `data/homework.json` i wczytywane przy uruchomieniu aplikacji. Zmiany zapisują się automatycznie. Przycisk „Zapisz” pozwala również zapisać je ręcznie lub ponowić zapis po błędzie.

## Wersja tekstowa

Wersja uruchamiana przez `main.py` udostępnia ponumerowane menu. Wpisz numer wybranej opcji i naciśnij Enter. Oprócz obsługi zadań możesz wyświetlić statystyki: liczbę wszystkich, wykonanych, niewykonanych i zaległych zadań. Opcja `0` kończy program.

## Wersja ćwiczeniowa

Projekt zawiera funkcje oznaczone komentarzami TODO. Opisane operacje będą działać w pełni po ich uzupełnieniu. Rozwiązania znajdują się w pliku [README_ROZWIAZANIA.md](README_ROZWIAZANIA.md).
