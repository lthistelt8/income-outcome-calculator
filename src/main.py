"""
Business logic that the user will execute through an implemented main menu
"""

from src.expense_entry import get_expense_detail, Category

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
        print(f"{i}. =={cat}==")

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
            print(f"{e}. {exp['expense name']} - ${exp['expense amount']:.2f}")

        print("Enter the corresponding expense number.")
        eidx = int(input("> "))
        if eidx == 0:
            print("Edit cancelled.")
            return None

        if not 1 <= eidx <= len(list(expenses[selected_cidx])):
            print(f"Selection out of range. Please select 1-{len(expenses[selected_cidx])}.")
            continue

        selected_eidx = list(expenses[selected_cidx])[eidx - 1]
        print(f"\nNow editing {selected_eidx['expense name']}.")
        print("Enter new expense name, or Enter to keep the current name.")
        new_exp_name = input("> ").strip()
        if new_exp_name == "":
            new_exp_name = selected_eidx['expense name']

        while True:
            print("Enter new expense amount, or Enter to keep the current value.")
            new_exp_amount = input("> ").strip()

            if new_exp_amount == "": #check for "Enter" input before validating float type
                new_exp_amount = selected_eidx['expense amount']
                break

            try:
                new_exp_amount = float(new_exp_amount)
                break
            except ValueError:
                print("Please enter a numerical value.")

            break

        print(
            f"{new_exp_name} - ${new_exp_amount:.2f} in {selected_cidx}? (y/n)"
        )
        print("Update expense?")

        while True:
            confirm = str(input("> "))
            if confirm not in ('y', 'n'):
                print("Invalid input. Enter 'y' or 'n'.")
                continue

            if confirm == 'n':
                print("Edit cancelled.")
                print("Returning to main menu...")
                break

            print(cidx, new_exp_name, new_exp_amount)
            return cidx, new_exp_name, new_exp_amount


add_expense()
print("==")
show_grouped_expenses()
print("==")
edit_expense()
print("==")
show_grouped_expenses()