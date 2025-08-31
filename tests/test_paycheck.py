from main import add_expense

test_expenses = {}

def test_add_expense():
    add_expense('Fixed', 'Mortgage', 90)
    assert 'Fixed' in test_expenses['category']
    assert 'Mortgage' in test_expenses['expense_name']
    assert 90 in test_expenses['expense_amount']
    