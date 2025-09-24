"""
Contains test functions for source code + business logic
"""
import unittest as u
from unittest.mock import Mock, patch
from src.expenses import expenses, Category
from src.main import add_expense_core, pop_expense, del_expense_core, update_expense_core
from src.data_entry import del_expense


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

    ##--DUPLICATE EXPENSE
    def assert_add_duplicate_name(self, cat):
        first_expense = add_expense_core(cat, 'Test', 4)
        second_expense = add_expense_core(cat, 'Test', 5)

        self.assertEqual(first_expense, second_expense)

    def test_add_duplicate_name(self):
        """
        Test add_expense() function in cases where the expense name matches.
        """

        self.run_on_categories(self.assert_add_duplicate_name)


    ##--CXL ADDING EXPENSE--
    def assert_add_graceful_exit(self, cat):
        cxl = add_expense_core(0,'Exit', 1 )

        self.assertIsNone(cxl)

    def test_add_graceful_exit(self):
        self.run_on_categories(self.assert_add_graceful_exit)

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
    def assert_update_expense_name_only(self, cat):
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

    def test_update_expense_name_only(self):
        self.run_on_categories(self.assert_update_expense_name_only)

    def assert_update_no_change(self, cat):
        first_expense = add_expense_core(cat, 'test', 2.0)
        second_expense = update_expense_core(cat, 'test', 'test', 2.0)

        self.assertEqual(first_expense, second_expense)
        self.assertNotIn(first_expense, expenses[cat])
        self.assertIn('test', expenses[cat])

    def test_update_no_change(self):
        self.run_on_categories(self.assert_update_no_change)

    ##--INVALID CASES--
    def assert_update_invalid_cat(self, cat):
        add_expense_core('', 'test', 2.0)
        update_expense_core('', 'test', 'pytest', 2.0)

        self.assertNotIn(cat, expenses)

    def test_update_invalid_cat(self):
        self.run_on_categories(self.assert_update_invalid_cat)

    def assert_update_invalid_value(self, cat):
        add_expense_core(cat, 'test', 2.0)

        self.assertRaises(TypeError, update_expense_core(cat, 'test', 'pytest', 'two'))

    def test_update_invalid_value(self):
        self.run_on_categories(self.assert_update_invalid_value)

class TestDeleteExpense(TestExpense):
    def assert_del_expense(self, cat):
        add_expense_core(cat, 'test', 2.0)
        self.assertIn('test', expenses[cat])

        del_expense_core(cat, 'test')
        self.assertNotIn('test', expenses[cat])

    def test_del_expense(self):
        self.run_on_categories(self.assert_del_expense)

#--INVALID DIDX--
    def assert_del_expense_invalid_didx(self, cat):
        add_expense_core(cat, 'test', 2.0)
        self.assertIn('test', expenses[cat])
        self.assertNotIn('n', expenses[cat], "'n' does not exist.")

    def test_del_expense_invalid_didx(self):
        self.run_on_categories(self.assert_del_expense_invalid_didx)

#--GRACEFUL CXL CATEGORY
    def assert_del_expense_graceful_cxl_cat(self, cat):
        add_expense_core(cat, 'test', 2.0)

        with patch("builtins.input", side_effect=[0]):
            del_cidx = del_expense()
            self.assertEqual(del_cidx, None)

    def test_del_expense_graceful_cxl_cat(self):
        self.run_on_categories(self.assert_del_expense_graceful_cxl_cat)

    def test_del_expense_graceful_cxl(self):
        self.run_on_categories(self.assert_del_expense_graceful_cxl)
