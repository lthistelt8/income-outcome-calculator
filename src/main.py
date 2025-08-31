'''
Business logic that the user will execute through an implemented main menu
'''

from enum import Enum, auto
from expense_entry import get_expense_detail
class CATEGORY(Enum):
    '''A list of enumerated categories for expenses'''
    AUTOMATIC=  auto()
    VARIABLE = auto()
    CREDIT_CARD = auto()
    ONE_TIME_EXPENSE = auto()

    def __str__(self):
        return self.name.replace("_"," ").title()

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
