"""
Superclass `TestExpense` for tests relating to adding, updating, deleting expenses
"""
import unittest as u
from src.expenses import expenses, Category

class TestExpense(u.TestCase):
    """Test business logic for expenses"""

    def initial(self):
        expenses.clear()
        expenses.update({cat: {} for cat in Category})

    def run_on_categories(self, func):
        """Handles iteration of each category per test"""
        for cat in Category:
            with self.subTest(cat = cat):
                #each iteration is tested on its own
                #failures are specific, and do not stop remaining tests
                self.initial()
                func(cat)
                #each function is passed with category parameters
