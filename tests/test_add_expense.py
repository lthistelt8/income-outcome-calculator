from tests.test_paycheck import TestExpense, Category, expenses
from unittest.mock import patch
from src.main import add_expense
from src.data_entry.data_entry import get_expense_detail

class TestAddExpense(TestExpense):
    def assert_get_expense_detail(self, cat):
        cat_list = str(list(Category).index(cat) + 1)
        #represents the number; 'cat' represents the keyword

        with patch("builtins.input", side_effect=[cat_list, 'first expense', 1.00, '20-11', 'y']) as expense_detail:
            exp_deet = get_expense_detail()
            self.assertEqual(exp_deet, (cat, 'First Expense', 1.00, '20-Nov'))

            self.assertEqual(expense_detail.call_count, 5)

    def test_get_expense_detail(self):
        """Test the add_expense() function"""

        self.run_on_categories(self.assert_get_expense_detail)

    ##--CXL EXP DETAIL AMOUNT--
    def assert_get_expense_detail_cxl_amount(self, cat):
        cat_list = str(list(Category).index(cat) + 1)
        with patch("builtins.input", side_effect=[cat_list, 'frist expnse', 0]) as canceled_detail_amount:
            cxl_exp_amount = get_expense_detail()
            self.assertIsNone(cxl_exp_amount)
            self.assertNotIn('frist expnse', expenses)

            self.assertEqual(canceled_detail_amount.call_count, 3)

    def test_get_expense_detail_cxl_amount(self):
        self.run_on_categories(self.assert_get_expense_detail_cxl_amount)

    ##--CXL EXP DETAIL NAME--
    def assert_get_expense_detail_cxl_name(self, cat):
        cat_list = str(list(Category).index(cat) + 1)
        with patch("builtins.input", side_effect=[cat_list, 0]) as canceled_detail_name:
            cxl_exp_name = get_expense_detail()
            self.assertIsNone(cxl_exp_name)

            self.assertEqual(canceled_detail_name.call_count, 2)

    def test_get_expense_detail_cxl_name(self):
        self.run_on_categories(self.assert_get_expense_detail_cxl_name)

    #--CXL EXP DETAIL CAT
    def assert_get_expense_detail_cxl_cat(self, cat):
        with patch("builtins.input", side_effect=[0]) as canceled_detail_category:
            cxl_cat = get_expense_detail()
            self.assertIsNone(cxl_cat)

            self.assertEqual(canceled_detail_category.call_count, 1)

    def test_get_expense_detail_cxl_cat(self):
        self.run_on_categories(self.assert_get_expense_detail_cxl_cat)

class TestAddIntegration(TestExpense):
    def assert_successful_add_once(self, cat):

        cat_list = str(list(Category).index(cat) + 1)
        with patch("builtins.input", side_effect=[cat_list, 'Pie', 3.14, '20-11', 'y']) as expense_info:
            add_expense()
            self.assertIn('Pie', expenses[cat])
            self.assertEqual(expenses[cat]['Pie'], {'expense_amount': 3.14, 'due_date': '20-Nov'})

            self.assertEqual(expense_info.call_count, 5)

    def test_successful_add_once(self):
        self.run_on_categories(self.assert_successful_add_once)

    #Invalid -> Valid Amount
    def assert_add_invalid_valid_exp_amount(self, cat):
        #invalid amount
        with patch("builtins.input", side_effect=[cat, 'no good', 'one dollar', '0']) as bad_add:
            add_expense()
            self.assertNotIn('no good', expenses[cat])

            self.assertEqual(bad_add.call_count, 4)

        #valid amount
        cat_list = str(list(Category).index(cat) + 1)

        with patch("builtins.input", side_effect=[cat_list, 'good', 1, '20-11','y']) as good_add:
            add_expense()
            self.assertIn('good', expenses[cat])
            self.assertEqual(expenses[cat]['Good'], {'expense_amount': 1.00, 'due_date': '20-Nov'})

            self.assertEqual(good_add.call_count, 5)

    def test_add_invalid_valid_amount(self):
        self.run_on_categories(self.assert_add_invalid_valid_exp_amount)

    #Invalid -> Valid Category
    def assert_add_invalid_valid_exp_category(self, cat):

        #invalid cat
        with patch("builtins.input", side_effect=['Auto', 'Automatic', 0]) as invalid_cat:
            bad_cat = get_expense_detail()
            self.assertIsNone(bad_cat)
            self.assertEqual(invalid_cat.call_count, 3)

        #valid cat
        cat_list = str(list(Category).index(cat) + 1)
        with patch("builtins.input", side_effect=[cat_list, 'good add', 3.21, '20-11' ,'y']) as valid_cat:
            good_cat = get_expense_detail()
            self.assertIsInstance(good_cat, tuple)
            self.assertEqual(good_cat, (cat, 'Good Add', 3.21, '20-Nov'))
            self.assertEqual(valid_cat.call_count, 5)

    def test_add_invalid_valid_cat_category(self):
        self.run_on_categories(self.assert_add_invalid_valid_exp_category)