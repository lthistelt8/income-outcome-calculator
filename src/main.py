"""
Business logic that the user will execute through an implemented main menu
"""

from src.expense_entry import get_expense_detail, Category

expenses: dict[Category, dict[str, float]] = {}
#expenses format: a dictionary of Categories, which is another dictionary of [str, float] formatted key:pairs

def group_expenses(expense_list):
    if isinstance(expense_list, dict):
        return expenses
    return {}

def show_grouped_expenses():
    grouped_expenses: dict = group_expenses(expenses)

    for cat in grouped_expenses:
        print(f"\n=={cat}==", type(grouped_expenses[cat]))
        #debug text; displays the data type of the category within 'grouped_expenses'
        for (name, amount) in grouped_expenses[cat].items():
            #for each name:amount pair in each category of grouped expenses
            print(f"{name} - ${amount:.2f}")


def add_expense():
    category, expense_name, expense_amount = get_expense_detail()
    #values assigned to function can immediately be called

    add_expense_core(category, expense_name, expense_amount)
    #aforementioned values are used to execute this function call

def add_expense_core(category, expense_name, expense_amount):
    """Handles the actual mutation of expenses dictionary"""
    expenses.setdefault(category, {})
    expenses[category][expense_name] = expense_amount #properly creates a dict of dicts
    # in the "category" dict, the "expense_name" is set to the "expense_amount"

def del_expense():
    """Delete expenses - not yet implemented"""
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

            return selected_didx




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

        new_exp_name = input("> ").strip()
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

def update_expense():
    category, former_expense, new_expense_name, new_expense_amount = edit_expense()
    new_expense_amount = float(new_expense_amount)

    update_expense_core(category, former_expense, new_expense_name, new_expense_amount)
    #values will update regardless of user input

    print(
        f"Updated expense: {new_expense_name} - ${new_expense_amount:.2f}"
    )

def update_expense_core(category, former_expense, new_expense, new_amount):
    """Deletes old expense, replaces it with updated expense"""

    expenses[category].pop(former_expense, None)
    #deletes old expense
    expenses[category][new_expense] = new_amount

def debug_menu(): #placeholder for a proper menu, which will eventually be extracted and fleshed out
    #as its own module
    """Manually run functions to verify user functionality."""
    print("**ADD EXPENSE**")
    add_expense()
    print("\n**SHOW EXPENSES**")
    show_grouped_expenses()
    print("\n**UPDATE EXPENSE**")
    update_expense()
    print("\n**SHOW UPDATED EXPENSE**")
    show_grouped_expenses()
