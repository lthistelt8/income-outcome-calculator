'''
Contains test functions for source code + business logic
'''
from unittest.mock import patch
import src.main as m

def test_add_expense():
    '''Test the add_expense() function'''

    test_expenses = {}

    m.add_expense('Fixed', 'Mortgage', 90)
    assert 'Fixed' in test_expenses['category']
    assert 'Mortgage' in test_expenses['expense name']
    assert 90 in test_expenses['expense amount']
    print(test_expenses)

print(f"\nWorking Directory: {WORKING_PATH}")
