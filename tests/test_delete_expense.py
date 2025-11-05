from tests.test_paycheck import TestExpense, Category, expenses
from unittest.mock import patch
from src.main import delete_expense, add_expense_core
from src.data_entry import del_expense

class TestDeleteExpense(TestExpense):
    def assert_del_expense(self, cat):
        add_expense_core(cat, 'test', 2.0)

        cat_list = str(list(Category).index(cat) + 1)
        with patch("builtins.input", side_effect=[cat_list, 1, 'y']) as deleted_expense:
            del_exp = del_expense()
            self.assertEqual(del_exp, (cat, 'test'))

            self.assertEqual(deleted_expense.call_count, 3)

    def test_del_expense(self):
        self.run_on_categories(self.assert_del_expense)

class TestDeleteIntegration(TestExpense):
    def assert_delete_expense_successful(self, cat):
        add_expense_core(cat, 'old expense', 1.0)

        cat_list = str(list(Category).index(cat) + 1)
        with patch("builtins.input", side_effect=[cat_list, 1, 'y']) as delete_expense_success:
            del_expense()
            self.assertNotIn('Old Expense', expenses[cat])

    def test_del_expense_successful(self):
        self.run_on_categories(self.assert_delete_expense_successful)

    #Invalid -> Valid Delete
    def assert_del_invalid_valid_exp(self, cat):
        add_expense_core(cat, 'old expense', 1.0)

        cat_list = str(list(Category).index(cat) + 1)
        with patch("builtins.input", side_effect=[5, cat_list, 2, 1, 'nah', 'y']) as invalid_valid_delete:
            del_expense()
            self.assertNotIn('Old Expense', expenses[cat])

            self.assertEqual(invalid_valid_delete.call_count, 6)

    def test_del_invalid_valid_exp(self):
        self.run_on_categories(self.assert_del_invalid_valid_exp)

    #CXL Expense
    def assert_del_exp_cxl(self, cat):
        add_expense_core(cat, 'old expense', 1.0)

        cat_list = str(list(Category).index(cat) + 1)
        with patch("builtins.input", side_effect=[cat_list, 1, 'n']) as cxl_expense:
            cxl_exp = delete_expense()
            self.assertIsNone(cxl_exp)

            self.assertIn('old expense', expenses[cat])
            self.assertEqual(cxl_expense.call_count, 3)

    def test_del_exp_cxl(self):
        self.run_on_categories(self.assert_del_exp_cxl)
