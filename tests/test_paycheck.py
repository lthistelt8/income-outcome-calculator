"""
Contains test functions for source code + business logic
"""
import unittest as u
from src.main import expenses, add_expense_core, del_expense, update_expense_core, Category


class TestExpense(u.TestCase):
    """Test business logic for expenses"""

    def initial(self):
        self.expenses = {}

    def test_add_expense(self):
        """Test the add_expense() function"""

        for cat in Category:
            with self.subTest(cat = cat):
                #subTest will run tests across all four categories
                self.initial()

                add_expense_core(cat, 'test', 2.0)

                self.assertIn(cat, expenses)
                self.assertIn('pytest', expenses[cat])
                self.assertEqual(expenses[cat]['pytest'], 2.0)


    def test_del_expense_empty_expenses(self):
        """Test the del_expense() function"""
        #requires dummy expenses, or save a test version of expenses
        del_expense()

    def test_edit_expense_name_only(self):
        """Test edit_expense() function when only the name is changed"""

        for cat in Category:
            with self.subTest(cat = cat):
                self.initial()

                add_expense_core(cat, 'test', 2.0)
                #will run same test with all four categories

                update_expense_core(cat, 'test', 'pytest', 2.0)

                self.assertIn(cat, expenses)
                #asserts that categories exist in expenses

                self.assertIn('pytest', expenses[cat])
                #asserts that 'pytest' appears in the categories

                self.assertEqual(expenses[cat]['pytest'], 2.0)
                #asserts that the value of 'pytest' in the expenses' categories all equal 2.0

                self.assertNotIn('test', expenses[cat])
                #asserts that 'test' has been removed from the expense dictionary