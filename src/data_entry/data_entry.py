"""Take user input to return as parameters to pass through business logic"""
from src.expenses import expenses, Category
from datetime import datetime, timedelta, time


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
        try:
            cidx = int(input("> "))
        except ValueError:
            print("Invalid input. Please enter the corresponding number.")
            continue

        if cidx == 0:
            print("Cancelled expense.")
            return None

        if not 1 <= cidx <= len(list(Category)):
            print(f"Selection out of range. Please select 1-{len(Category)}.")
            continue

        break

    cat = list(Category)[cidx - 1]

    print("Enter the expense name.")
    expense_name = str(input("> ")).title()
    if expense_name == "0":
        print("Cancelled expense.")
        return None

    if expense_name in expenses:
        print(
            f"'{expense_name}' already exists. Would you like to update '{expense_name}' instead? (y/n)")
        while True:
            update = str(input("> "))

            if update not in ('y', 'n'):
                print("Invalid input. Please enter 'y' or 'n'.")
                continue
            if update == 'n':
                print(f"Note: there will be duplicate entries of {expense_name}.")
                break

            edit_expense()
            break


    while True:
        print("Enter expense amount.")

        try:
            expense_amount = float(input("> "))
            if expense_amount == 0:
                print("Cancelled expense.")
                return None
        except (TypeError, ValueError):
            print("Please enter a numerical value.")
            continue
        break

    print(f"Expense: {expense_name}, {expense_amount}, in {cat} expenses.") #expense_amount is properly referenced, need to determine how to override warning
    print("Confirm expense? (y/n)")
    while True:
        confirm = str(input("> "))

        if confirm not in ('y', 'n'):
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        if confirm == 'n':
            get_expense_detail()

        print(cat, expense_name, expense_amount) #debug text

        return cat, expense_name, expense_amount

def del_expense():
    """Collects input to pass through helper functions"""
    if not any(expenses.values()):
        print("No expenses available for deletion.")
        return None

    for i, cat in enumerate(Category, 1):
        print(f"{i}. =={cat}==")

    print("Enter the corresponding category number, or 0 to cancel at any time.")
    while True:
        try:
            cidx = int(input("> "))
        except ValueError:
            print("Invalid input. Enter the corresponding category number.")
            continue

        if cidx == 0:
            print("Deletion cancelled.")
            return None

        if not 1 <= cidx <= len(list(Category)):
            print(f"Selection out of range. Enter 1-{len(list(Category))}.")
            continue

        selected_cidx = list(Category)[cidx - 1] #type:ignore
        for e, (name, amount) in enumerate(expenses[selected_cidx].items(), 1):
            print(f"{e}. {name} - ${amount:.2f}")

        print("Enter the corresponding expense number.")
        while True:
            try:
                didx = int(input("> "))
            except ValueError:
                print("Invalid input. Enter the corresponding expense number.")
                continue

            if didx == 0:
                print("Deletion cancelled.")
                return None

            if not 1 <= didx <= len(list(expenses[selected_cidx])):
                print(f"Selection out of range. Please select 1-{len(expenses[selected_cidx])}.")
                continue
            break

        name, amount = list(expenses[selected_cidx].items())[didx - 1]

        print(f"{name} - ${amount:.2f}")
        while True:
            print(f"Confirm deletion of {name}? DELETION IS IRREVERSIBLE (y/n).")

            confirm = str(input("> "))
            if confirm not in ('y', 'n'):
                print("Invalid response. Please enter 'y' or 'n'.")
                continue

            if confirm == 'n':
                print("Deletion cancelled.")
                return None

            return selected_cidx, name

def edit_expense():
    """Edit expense details."""
    if not any(expenses.values()):
        print("No expenses to edit.")
        return None

    for i, cat in enumerate(Category, 1):
        print(f"{i}. =={cat}==")

    #CATEGORY SELECTION
    print("Enter the corresponding category number, or 0 to cancel at any time.")
    while True:
        try:
            cidx = int(input("> "))
        except ValueError:
            print("Invalid input. Enter the corresponding number, or 0 to cancel.")
            continue
        if cidx == 0:
            print("Edit cancelled.")
            return None

        if not 1 <= cidx <= len(Category):
            print(f"Selection out of range. Please select 1-{len(Category)}.")
            continue

        selected_cidx = list(Category)[cidx - 1]

        #EXP SELECTION
        exp = list(expenses.get(selected_cidx, {}).items())
        #fetches dict for selected category, returns name/amount pair
        #then turns it into an index

        if not exp:
            print(f"No expenses in {selected_cidx}.")
            return None

        for e, (exp_name, exp_amount) in enumerate(exp, 1):
            print(f"{e}. {exp_name} - ${exp_amount:.2f}")

        print("Enter the corresponding expense number.")
        while True:
            try:
                eidx = int(input("> "))
            except ValueError:
                print("Invalid input. Enter the corresponding number, or 0 to cancel.")
                continue

            if eidx == 0:
                print("Edit cancelled.")
                return None

            if not 1 <= eidx <= len(exp):
                print(f"Selection out of range. Please select 1-{len(exp)}.")
                continue
            break

        current_name, current_amount = exp[eidx - 1]

        print(f"\nNow editing {current_name}.")

        #NEW EXPENSE NAME
        print("Enter new expense name, or Enter to keep the current name.")

        new_exp_name = input("> ").strip().title()
        if new_exp_name == "":
            new_exp_name = current_name
            #name is still equivalent to the earlier referenced 'name'

        #NEW EXPENSE AMOUNT
        while True:
            print("Enter new expense amount, or Enter to keep the current value.")
            new_exp_amount = input("> ")

            if new_exp_amount == "": #check for "Enter" input before validating float type
                new_exp_amount = float(current_amount)
                break

            try:
                new_exp_amount = float(new_exp_amount)
                #the new expense amount is validated as a float before being allowed to pass
            except ValueError:
                print("Please enter a numerical value.")
                continue
            break

        #VERIFY UPDATED EXPENSE
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

            print(selected_cidx, current_name, new_exp_name, new_exp_amount)
            #debug text; displays the values that are to be returned for use in 'update_expense'

            return selected_cidx, current_name, new_exp_name, new_exp_amount