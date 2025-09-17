"""
Contains test functions for source code + business logic
"""
import unittest as u
import unittest.mock as um
from src.main import expenses, add_expense_core, del_expense, edit_expense

class TestExpense(u.TestCase):
    """Test business logic for expenses"""

    def test_add_expense(self):
        """Test the add_expense() function"""

        expenses.clear()

        with um.patch('src.main.get_expense_detail', return_value = None):
            add_expense_core('Fixed', 'Mortgage', 90)

            assert 'Fixed' in expenses

            row = expenses['Fixed'][0]
            assert row ['expense name'] == 'Mortgage'
            assert row ['expense amount'] == 90

    def test_del_expense_empty_expenses(self):
        """Test the del_expense() function"""
        #requires dummy expenses, or save a test version of expenses
        del_expense()
