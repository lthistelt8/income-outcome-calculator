'''
Contains test functions for source code + business logic
'''
import src.main

def test_add_expense():
    '''Test the add_expense() function'''

    test_expenses = {}

    src.main.add_expense('Fixed', 'Mortgage', 90)
    assert 'Fixed' in test_expenses['category']
    assert 'Mortgage' in test_expenses['expense name']
    assert 90 in test_expenses['expense amount']
