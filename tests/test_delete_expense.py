from tests.test_paycheck import TestExpense
from unittest.mock import patch
from src.main import pop_expense
from src.data_entry import del_expense

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

#-- GRACEFUL CXL DIDX
    def assert_del_expense_graceful_cxl_didx(self, cat):
        add_expense_core(cat, 'test', 2.0)
        self.assertIn('test',expenses[cat])

        cat_list = str(list(Category).index(cat) + 1)
        #determines the index at which the user-input 'cat' is, then converts to string-equivalent

        with patch("builtins.input", side_effect=[cat_list, 0]) as m:
            del_eidx = del_expense()
            self.assertIsNone(del_eidx)
            self.assertEqual(m.call_count, 2)

    def test_del_expense_graceful_cxl_didx(self):
        self.run_on_categories(self.assert_del_expense_graceful_cxl_didx)

#--CONFIRM 'n' PROMPT
    def assert_del_expense_confirm_input_n(self, cat):
        add_expense_core(cat, 'test', 2.0)
        self.assertIn('test', expenses[cat])

        cat_list = str(list(Category).index(cat) + 1)

        with patch("builtins.input", side_effect=[cat_list, 0, 'n']) as m:
            no_del = del_expense()
            self.assertIsNone(no_del)
            self.assertEqual(m.call_count, 2)

    def test_del_expense_confirm_input_n(self):
        self.run_on_categories(self.assert_del_expense_confirm_input_n)

#--FAIL, THEN PASS
    def assert_del_expense_fail_pass(self, cat):
        add_expense_core(cat, 'test', 2.0)
        self.assertIn('test', expenses[cat])

        #fail phase - invalid cidx, then cxl input
        with patch("builtins.input", side_effect=['auto', '0']) as m_invalid:
            invalid_del = del_expense()
            self.assertIsNone(invalid_del)

            self.assertEqual(m_invalid.call_count, 2)
            #call counts refer to how many values are passed

        #success phase
        cat_list = str(list(Category).index(cat) + 1)

        with patch("builtins.input", side_effect=[cat_list, '1', 'y']) as m_valid:
            valid_del = del_expense()

            self.assertIsInstance(valid_del, tuple)
            #asserts that instances in valid_del are a tuple (cat_list, '1', 'y')

            self.assertEqual(valid_del, (cat, "test"))
            #asserts that 'valid_del' instance is equivalent to tuple (cat, 'test')

            self.assertEqual(m_valid.call_count, 3)

    def test_del_expense_fail_pass(self):
        self.run_on_categories(self.assert_del_expense_fail_pass)

class TestDeleteIntegration(TestExpense):
    def assert_del_expense_successful_once(self, cat):
        add_expense_core(cat, 'old expense', 1.0)

        cat_list = str(list(Category).index(cat) + 1)
        with patch("builtins.input", side_effect=[cat_list, 1, 'y']) as delete_expense:
            del_exp = del_expense()
            self.assertIsInstance(del_exp, tuple)
            self.assertEqual(del_exp, (cat, 'old expense'))

            del_expense_core(*del_exp)
            self.assertNotIn('old expense', expenses[cat])
            self.assertEqual(delete_expense.call_count, 3)

    def test_del_expense_successful_once(self):
        self.run_on_categories(self.assert_del_expense_successful_once)

    #Invalid -> Valid Delete
    def assert_del_invalid_valid_exp(self, cat):
        add_expense_core(cat, 'old expense', 1.0)

        cat_list = str(list(Category).index(cat) + 1)
        with patch("builtins.input", side_effect=[5, cat_list, 2, 1, 'nah', 'y']) as invalid_valid_delete:
            invalid_valid_exp = del_expense()
            self.assertIsInstance(invalid_valid_exp, tuple)
            self.assertEqual(invalid_valid_exp, (cat, 'old expense'))

            del_expense_core(*invalid_valid_exp)
            self.assertNotIn('old expense', expenses[cat])
            self.assertEqual(invalid_valid_delete.call_count, 6)

    def test_del_invalid_valid_exp(self):
        self.run_on_categories(self.assert_del_invalid_valid_exp)

    #CXL Expense
    def assert_del_exp_cxl(self, cat):
        add_expense_core(cat, 'old expense', 1.0)

        cat_list = str(list(Category).index(cat) + 1)
        with patch("builtins.input", side_effect=[cat_list, 1, 'n']) as cxl_expense:
            cxl_exp = del_expense()
            self.assertIsNone(cxl_exp)

            self.assertIn('old expense', expenses[cat])
            self.assertEqual(cxl_expense.call_count, 3)

    def test_del_exp_cxl(self):
        self.run_on_categories(self.assert_del_exp_cxl)