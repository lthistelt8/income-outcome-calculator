'''
Contains test functions for source code + business logic
'''
from pathlib import Path as p
import src.main as s

def pathfinder():
    '''Displays working path to test module'''
    working_path = p(__file__).parent
    print(f"\nWorking Directory: {working_path}")

def test_add_expense():
    '''Test the add_expense() function'''

    test_expenses = {}

    s.add_expense('Fixed', 'Mortgage', 90)
    assert 'Fixed' in test_expenses['category']
    assert 'Mortgage' in test_expenses['expense name']
    assert 90 in test_expenses['expense amount']
    print(test_expenses)

pathfinder()
