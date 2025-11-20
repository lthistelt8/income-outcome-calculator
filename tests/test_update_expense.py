from tests.test_paycheck import TestExpense, Category, expenses
from unittest.mock import patch
from src.main import update_expense, add_expense_core
from src.data_entry.data_entry import edit_expense

class TestUpdateExpense(TestExpense):
    def assert_edit_expense_name(self, cat):
        add_expense_core(cat, 'test', 2.0, due_date)
        #will run same test with all four categories

        cat_list = str(list(Category).index(cat) + 1)
        with patch("builtins.input", side_effect=[cat_list, 1, 'pytest', '', 'y']) as edited_expense:
            edit_exp = edit_expense()
            self.assertEqual(edit_exp, (cat, 'test', 'Pytest', 2.0))

            self.assertEqual(edited_expense.call_count, 5)

    def test_update_expense_name_only(self):
        self.run_on_categories(self.assert_edit_expense_name)

    def assert_edit_no_change(self, cat):
        add_expense_core(cat, 'test', 2.0, due_date)

        cat_list = str(list(Category).index(cat) + 1)
        with patch("builtins.input", side_effect=[cat_list, 1, '', '', 'y']) as edit_expense_no_change:
            no_chg_exp = edit_expense()
            self.assertEqual(no_chg_exp, (cat, 'test', 'test', 2.0))

            self.assertEqual(edit_expense_no_change.call_count, 5)

    def test_update_no_change(self):
        self.run_on_categories(self.assert_edit_no_change)

class TestUpdateIntegration(TestExpense):
    def assert_successful_update(self, cat):

        cat_list = str(list(Category).index(cat) + 1)
        add_expense_core(cat, "un-updated expense", 2, due_date)

        with patch("builtins.input", side_effect=[cat_list, 1, "updated expense", 20, "y"]) as updated_expense:
            update_expense()
            self.assertIn('Updated Expense', expenses[cat])
            self.assertNotIn('Un-Updated Expense', expenses[cat])
            self.assertEqual(expenses[cat]['Updated Expense'], 20.00)

            self.assertEqual(updated_expense.call_count, 5)

    def test_successful_update_once(self):
        self.run_on_categories(self.assert_successful_update)

    #Invalid -> Valid Update
    def assert_update_invalid_valid_exp(self, cat):
        cat_list = str(list(Category).index(cat) + 1)
        add_expense_core(cat, "new expense", 2, due_date)

        with patch("builtins.input", side_effect=[5, cat_list, 2, 1, 'updated expense', 'three', 3, 'y']) as invalid_valid_update:
            update_expense()
            self.assertIn('Updated Expense', expenses[cat])
            self.assertEqual(expenses[cat]['Updated Expense'], 3.00)

            self.assertEqual(invalid_valid_update.call_count, 8)

    def test_update_invalid_valid_exp(self):
        self.run_on_categories(self.assert_update_invalid_valid_exp)