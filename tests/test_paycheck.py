'''
Contains test functions for source code + business logic
'''
from unittest.mock import patch
import src.main as m

def test_add_expense():
    '''Test the add_expense() function'''

    m.expenses.clear()

    with patch('src.main.get_expense_detail', return_value = None):
        m.add_expense('Fixed', 'Mortgage', 90)

        assert 'Fixed' in m.expenses

        row = m.expenses['Fixed'][0]

        assert row ['expense name'] == 'Mortgage'
        assert row ['expense amount'] == 90

def test_del_expense_empty_expenses():
    '''Test the del_expense() function'''
    #requires dummy expenses, or save a test version of expenses
    m.expenses.clear()
