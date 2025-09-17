"""
Business logic that the user will execute through an implemented main menu
"""

from src.expense_entry import get_expense_detail

expenses = {}

def group_expenses(expenses):
    if isinstance(expenses, dict):
        return expenses
    return "No expenses found."

def show_grouped_expenses():
    grouped_expenses = group_expenses(expenses)

    for cat in grouped_expenses:
        print(f"\n=={cat}==")
        for exp in grouped_expenses[cat]:
            if isinstance(exp, dict):
                print(
                    f"* {exp['expense name']}: ${exp['expense amount']:.2f}"
                )
            else:
                print("Unexpected:", type(exp), exp)



def add_expense():
    """
    Parameters are passed from get_expense_detail() as arguments to create an expense dictionary object.
    """
    category, expense_name, expense_amount = get_expense_detail()
    expense = {
        'category': category,
        'expense name': expense_name,
        'expense amount': expense_amount
    }

    expenses.setdefault(category, []).append(expense)

def del_expense():
    """Delete expenses - not yet implemented"""
    print("Feature not yet implemented: delete expense.")
    return None

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

        selected_eidx = list(expenses[selected_cidx])[eidx - 1]
        print(f"Now editing {selected_eidx}.")

add_expense()
show_grouped_expenses() #debug text