"""Take user input to return as parameters to pass through business logic"""

from enum import StrEnum, auto
from src.main import expenses

class Category(StrEnum):
    """A list of enumerated categories for expenses"""
    AUTOMATIC = auto()
    VARIABLE = auto()
    CREDIT_CARD = auto()
    ONE_TIME_EXPENSE = auto()

    def __str__(self):
        return self.name.replace("_", " ").title()

def get_expense_detail():
    """Collects and returns expense details.
    Parameters:
        Category (represented by an integer category index, or 'cidx')
        Expense name (represented by a string)
        Expense amount (represented by a float)
    """
    for i, cat in enumerate(Category, 1):
        print(f"{i}. {cat}")

    print("Enter the category number for this expense (or 0 to cancel at any point).")

    while True:
        cidx = int(input("> "))
        if cidx == 0:
            print("Cancelled expense.")
            return None

        if not 1 <= cidx <= len(list(Category)):
            print(f"Selection out of range. Please select 1-{len(Category)}.")
            continue

        break

    cat = list(Category)[cidx - 1]

    print("Enter the expense name.")
    expense_name = str(input("> "))
    if expense_name == "0":
        print("Cancelled expense.")
        return None

    while True:
        print("Enter expense amount.")

        try:
            expense_amount = float(input("> "))
            if expense_amount == 0:
                print("Cancelled expense.")
                return None
        except ValueError:
            print("Please enter a numerical value.")
            continue
        break

    print(f"Expense: {expense_name}, {expense_amount}, in {cat} expenses.")
    print("Confirm expense? (y/n)")
    while True:
        confirm = str(input("> "))

        if confirm not in ('y', 'n'):
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        if confirm == 'n':
            return get_expense_detail

        return cat, expense_name, expense_amount

def edit_expense():
    """Edit expense details."""
    if not any(expenses.values()):
        print("No expenses to edit.")
        return None

    for i, cat in enumerate(Category, 1):
        print(f"{i}. {cat}")

    print("Enter the corresponding category number, or 0 to cancel at any time.")
    while True:
        cidx = int(input("> "))
        if cidx == 0:
            print("Edit cancelled.")
            return None

        if not 1 <= cidx <= len(list(Category)):
            print(f"Selection out of range. Please select 1-{len(Category)}.")
            continue

        selected_cidx = list(Category)[cidx - 1]
        for e, exp in enumerate(expenses[selected_cidx], 1):
            print(f"{e}. {exp}")

        print("Enter the corresponding expense number.")
        eidx = int(input("> "))
        if eidx == 0:
            print("Edit cancelled.")
            return None

        if not 1 <= eidx <= len(list(expenses[selected_cidx])):
            print(f"Selection out of range. Please select 1-{len(expenses[selected_cidx])}.")
            continue
