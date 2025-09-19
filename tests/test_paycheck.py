"""
Contains test functions for source code + business logic
"""
import unittest as u
from src.expenses import expenses, Category
from src.main import add_expense_core, del_expense_core, update_expense_core


class TestExpense(u.TestCase):
    """Test business logic for expenses"""

    def initial(self):
        expenses.clear()

    def run_on_categories(self, func):
        """Handles iteration of each category per test"""
        for cat in Category:
            with self.subTest(cat = cat):
                #each iteration is tested on its own
                #failures are specific, and do not stop remaining tests
                self.initial()
                func(cat)
                #each function is passed with category parameters

class TestAddExpense(TestExpense):
    def assert_add(self, cat):
        add_expense_core(cat, 'test', 2.0)

        self.assertIn(cat, expenses)
        self.assertIn('test', expenses[cat])
        self.assertEqual(expenses[cat]['test'], 2.0)

    def test_add_expense(self):
        """Test the add_expense() function"""

        self.run_on_categories(self.assert_add)

    ##--INVALID CASES--

    #Invalid Category
    def assert_add_invalid_category(self, cat):
        add_expense_core('', 'Test', 2.0)

        self.assertNotIn(cat, expenses)

    def test_add_invalid_category(self):
        self.run_on_categories(self.assert_add_invalid_category)

    #Invalid Value
    def assert_add_invalid_value(self, cat):
        self.assertRaises(TypeError, add_expense_core(cat, 'Empty', 'test'))

    def test_add_invalid_value(self):
        self.run_on_categories(self.assert_add_invalid_value)



class TestUpdateExpense(TestExpense):
    def initial(self):
        super().initial()

    def test_update_expense_name_only(self):
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

class TestDeleteExpense(TestExpense):
    def initial(self):
        super().initial()

    def test_del_expense(self):
        """Test the del_expense() function"""

        for cat in Category:
            with self.subTest(cat = cat):
                self.initial()

                add_expense_core(cat, 'test', 2.0)
                del_expense_core(cat, 'test')

                self.assertNotIn('test', expenses[cat])
                self.assertNotEqual(expenses[cat], 'test')

