'''
Business logic that the user will execute through an implemented main menu
'''

from .expense_entry import get_expense_detail

expenses = {}

def add_expense(category, expense_name, expense_amount):
    '''
    Arguments are pulled from the helper function to create and append an 'expense' dictionary.
    '''
    get_expense_detail()
    expense = {
        'category': category,
        'expense name': expense_name,
        'expense amount': expense_amount
    }

    expenses.setdefault(category, []).append(expense)

print(expenses)

def del_expense():
    '''Delete expenses'''
    if not expenses:
        print("No expenses found for deletion.")
        return None

    for e, expense in enumerate(expenses, 1):
        print(f"{e}. {expense['expense name']}")

    print("Enter the number corresponding to the expense you'd like to delete, or 0 to cancel.")
    while True:
        try:
            didx = int(input("> "))
            if didx == 0:
                print("Deletion cancelled.")
                break
        except ValueError:
            print("Invalid entry. Enter only the number associated with the expense.")
            continue

        if 1<= didx <= len(expenses):
            print(f"Selection out of range. Please enter 1-{len(expenses)}.")
            continue
        break

    marked = expenses[didx - 1]
    while True:
        print(f"Are you sure you want to delete {marked} (y/n)?")
        confirm = str(input("> "))
        if confirm not in ('y', 'n'):
            print("Invalid entry. Please enter 'y' or 'n'.")
            continue

        if confirm == 'n':
            print("Deletion cancelled.")
            break

    expenses.pop(marked)
    print(f"{marked} has been deleted.")
    return None
