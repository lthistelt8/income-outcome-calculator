from tests.test_paycheck import TestExpense

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

    def assert_update_invalid_then_valid(self, cat):
        add_expense_core(cat, 'old expense', 1.0)

        #invalid update
        with patch("builtins.input", side_effect=['old expense', 'first', 0]) as bad_update:
            invalid_update = edit_expense()
            self.assertIsNone(invalid_update)

            self.assertEqual(bad_update.call_count, 3)

        #valid update
        cat_list = str(list(Category).index(cat) + 1)
        with patch("builtins.input", side_effect=[cat_list, 1, 'new expense', 5, 'y']) as good_update:
            valid_update = edit_expense()
            self.assertIsInstance(valid_update, tuple)
            self.assertEqual(valid_update, (cat, 'old expense', 'New Expense', 5.0))

            self.assertEqual(good_update.call_count, 5)

    def test_update_invalid_then_valid(self):
        self.run_on_categories(self.assert_update_invalid_then_valid)

class TestUpdateIntegration(TestExpense):
    def assert_successful_update_once(self, cat):

        cat_list = str(list(Category).index(cat) + 1)
        add_expense_core(cat, "new expense", 2)

        with patch("builtins.input", side_effect=[cat_list, 1, "updated expense", "", "y"]) as updated_expense:
            edit_exp = edit_expense()
            self.assertIsInstance(edit_exp, tuple)
            self.assertEqual(edit_exp, (cat, "new expense", "Updated Expense", 2.0))

            update_expense_core(*edit_exp)
            self.assertIn("Updated Expense", expenses[cat])
            self.assertNotIn("New Expense", expenses[cat])
            self.assertEqual(updated_expense.call_count, 5)

    def test_successful_update_once(self):
        self.run_on_categories(self.assert_successful_update_once)

    #Invalid -> Valid Update
    def assert_update_invalid_valid_exp(self, cat):
        cat_list = str(list(Category).index(cat) + 1)
        add_expense_core(cat, "new expense", 2)

        with patch("builtins.input", side_effect=[5, cat_list, 2, 1, 'updated expense', 'three', 3, "y"]) as invalid_valid_expense:
            invalid_valid_exp = edit_expense()
            self.assertIsInstance(invalid_valid_exp, tuple)
            self.assertEqual(invalid_valid_exp, (cat, 'new expense', 'Updated Expense', 3.0))

            update_expense_core(*invalid_valid_exp)
            self.assertIn('Updated Expense', expenses[cat])
            self.assertNotIn('New Expense', expenses[cat])
            self.assertEqual(invalid_valid_expense.call_count, 8)

    def test_update_invalid_valid_exp(self):
        self.run_on_categories(self.assert_update_invalid_valid_exp)