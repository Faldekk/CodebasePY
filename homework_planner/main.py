from menu import run_menu
from storage import load_assignments


def main():
    assignments = load_assignments()
    run_menu(assignments)


if __name__ == "__main__":
    main()
