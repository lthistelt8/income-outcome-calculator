from tests.test_paycheck import TestExpense, Category, expenses
from unittest.mock import patch
from src.main import add_expense
from src.data_entry import get_expense_detail

class TestAddExpense(TestExpense):
    def assert_get_expense_detail(self, cat):
        cat_list = str(list(Category).index(cat) + 1)
        #represents the number; 'cat' represents the keyword

        with patch("builtins.input", side_effect=[cat_list, 'first expense', 1.00, 'y']) as first_expense:
            exp_one = get_expense_detail()
            self.assertEqual(exp_one, (cat, 'First Expense', 1.00))

            self.assertEqual(first_expense.call_count, 4)

    def test_add_expense(self):
        """Test the add_expense() function"""

        self.run_on_categories(self.assert_get_expense_detail)

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

class TestAddIntegration(TestExpense):
    def assert_successful_add_once(self, cat):

        cat_list = str(list(Category).index(cat) + 1)
        with patch("builtins.input", side_effect=[cat_list, 'Pie', 3.14, 'y']) as expense_info:
            add_expense()
            self.assertIn('Pie', expenses[cat])
            self.assertEqual(expenses[cat]['Pie'], 3.14)

            self.assertEqual(expense_info.call_count, 4)

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

        with patch("builtins.input", side_effect=[cat_list, 'good', 1, 'y']) as good_add:
            add_expense()
            self.assertIn('good', expenses[cat])
            self.assertEqual(expenses[cat]['Good'], 1.00)

            self.assertEqual(good_add.call_count, 4)

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
        with patch("builtins.input", side_effect=[cat_list, 'good add', 3.21, 'y']) as valid_cat:
            good_cat = get_expense_detail()
            self.assertIsInstance(good_cat, tuple)
            self.assertEqual(good_cat, (cat, 'Good Add', 3.21))
            self.assertEqual(valid_cat.call_count, 4)

    def test_add_invalid_valid_cat_category(self):
        self.run_on_categories(self.assert_add_invalid_valid_exp_category)