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
