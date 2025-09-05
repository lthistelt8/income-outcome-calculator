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
        assert 'Fixed' in m.expenses['category']
        assert 'Mortgage' in m.expenses['expense name']
        assert 90 in m.expenses['expense amount']
