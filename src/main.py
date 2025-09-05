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
