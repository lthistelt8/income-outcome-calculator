"""
Business logic that the user will execute through an implemented main menu
"""

from src.expense_entry import get_expense_detail, Category

expenses: dict = {}

def group_expenses(expense_list):
    if isinstance(expense_list, dict):
        return expenses
    return {}

def show_grouped_expenses():
    grouped_expenses: dict = group_expenses(expenses)

    for cat in grouped_expenses:
        print(f"\n=={cat}==", type(grouped_expenses[cat])) #debug text
        for (name, amount) in grouped_expenses[cat].items():
            print(f"{name} - ${amount:.2f}")




def add_expense():
    """
    Parameters are passed from get_expense_detail() as arguments to create an expense dictionary object.
    """
    category, expense_name, expense_amount = get_expense_detail()

    expenses.setdefault(category, {})
    expenses[category][expense_name] = expense_amount #properly creates a dict of dicts
    # in the "category" dict, the "expense_name" is set to the "expense_amount"

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
        for e, (name, amount) in enumerate(expenses[selected_cidx].items(), 1):
            print(f"{e}. {name} - ${amount:.2f}")


        print("Enter the corresponding expense number.")
        eidx = int(input("> "))
        if eidx == 0:
            print("Edit cancelled.")
            return None

        if not 1 <= eidx <= len(list(expenses[selected_cidx])):
            print(f"Selection out of range. Please select 1-{len(expenses[selected_cidx])}.")
            continue

        selected_eidx = list(expenses[selected_cidx])[eidx - 1]

        print(f"\nNow editing {str(selected_eidx)}.")
        print("Enter new expense name, or Enter to keep the current name.")

        new_exp_name = input("> ").strip()
        if new_exp_name == "":
            new_exp_name = name

        while True:
            print("Enter new expense amount, or Enter to keep the current value.")
            new_exp_amount = (input("> ").strip())

            if new_exp_amount == "": #check for "Enter" input before validating float type
                new_exp_amount = float(amount)
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

            print(selected_cidx, new_exp_name, new_exp_amount)
            return selected_cidx, new_exp_name, new_exp_amount

def update_expense():
    """Update expense data based on returned values from edit_expense()"""
    category, new_expense_name, new_expense_amount = edit_expense()
    #even if values are unchanged, this should properly update

    expenses[category][new_expense_name] = new_expense_amount
    print(
        f"Updated expense: {new_expense_name} - ${new_expense_amount:.2f}"
    )

def debug_menu():
    print("**ADD EXPENSE**")
    add_expense()
    print("\n**SHOW EXPENSES**")
    show_grouped_expenses()
    print("\n**UPDATE EXPENSE**")
    update_expense()
    print("\n**SHOW UPDATED EXPENSE**")
    show_grouped_expenses()

debug_menu()