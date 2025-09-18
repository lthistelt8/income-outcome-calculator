"""
Contains test functions for source code + business logic
"""
import unittest as u
import unittest.mock as um
from src.main import expenses, add_expense_core, del_expense, update_expense_core

class TestExpense(u.TestCase):
    """Test business logic for expenses"""

    def test_add_expense(self):
        """Test the add_expense() function"""

        expenses.clear()

        with um.patch('src.main.get_expense_detail', return_value = None):
            add_expense_core('Automatic', 'Mortgage', 90)

            assert 'Automatic' in expenses

            assert 'Mortgage' in expenses['Automatic']
            assert expenses['Automatic']['Mortgage'] == 90

    def test_del_expense_empty_expenses(self):
        """Test the del_expense() function"""
        #requires dummy expenses, or save a test version of expenses
        del_expense()

    def test_edit_expense_name_only(self):
        """Test edit_expense() function when only the name is changed"""

        expenses.clear()

        with um.patch('src.main.edit_expense', return_value = None):
            update_expense_core('Automatic', 'test', 'pytest', '2')

            assert 'Automatic' in expenses

            assert 'pytest' in expenses['Automatic']
            assert expenses['Automatic']['pytest'] == 2