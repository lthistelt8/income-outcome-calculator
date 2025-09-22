"""Take user input to return as parameters to pass through business logic"""
from src.expenses import expenses, Category


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
        except TypeError:
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
        cidx = int(input("> "))
        if cidx == 0:
            print("Deletion cancelled.")
            return None

        if not 1 <= cidx <= len(list(Category)):
            print(f"Selection out of range. Enter 1-{len(list(Category))}.")
            continue

        selected_cidx = list(Category)[cidx - 1]
        for e, (name, amount) in enumerate(expenses[selected_cidx].items(), 1):
            print(f"{e}. {name} - ${amount:.2f}")

        print("Enter the corresponding expense number.")
        didx = int(input("> "))
        if didx == 0:
            print("Deletion cancelled.")
            return None

        if not 1 <= didx <= len(list(expenses[selected_cidx])):
            print(f"Selection out of range. Please select 1-{len(expenses[selected_cidx])}.")
            continue

        selected_didx = list(expenses[selected_cidx])[didx - 1]

        for name, amount in selected_didx:
            print(f"{name} - ${amount:.2f}")

        while True:
            print(f"Confirm deletion of {name}? DELETION IS IRREVERSIBLE (y/n).")

            confirm = str(input("> "))
            if confirm not in ('y', 'n'):
                print("Invalid response. Please enter 'y' or 'n'.")
                continue

            if confirm == 'n':
                print("Deletion cancelled.")

            return selected_cidx, selected_didx

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
            #for dict of dicts, iterating through a list is fine, as long as
            #said list isn't then used to call a value
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
        #specifying 'str' prevents KeyErrors down the line
        print("Enter new expense name, or Enter to keep the current name.")

        new_exp_name = input("> ").strip().title()
        if new_exp_name == "":
            new_exp_name = name
            #name is still equivalent to the earlier referenced 'name'

        while True:
            print("Enter new expense amount, or Enter to keep the current value.")
            new_exp_amount = (input("> ").strip())

            if new_exp_amount == "": #check for "Enter" input before validating float type
                new_exp_amount = float(amount)
                break

            try:
                new_exp_amount = float(new_exp_amount)
                #the new expense amount is validated as a float before being allowed to pass
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

            print(selected_cidx, selected_eidx, new_exp_name, new_exp_amount)
            #debug text; displays the values that are to be returned for use in 'update_expense'
            return selected_cidx, selected_eidx, new_exp_name, new_exp_amount