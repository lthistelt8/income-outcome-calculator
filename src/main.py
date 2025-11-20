"""
Business logic that the user will execute through an implemented main menu
"""

from src.data_entry.data_entry import get_expense_detail, del_expense, edit_expense
from src.expenses import expenses, datetime

def group_expenses(expense_list):
    if isinstance(expense_list, dict):
        return expenses
    return {}

def show_grouped_expenses():
    grouped_expenses: dict = group_expenses(expenses)

    for cat in grouped_expenses:
        print(f"\n=={cat}==", type(grouped_expenses[cat]))
        #debug text; displays the data type of the category within 'grouped_expenses'
        for (name, amount) in grouped_expenses[cat].items():
            #for each name:amount pair in each category of grouped expenses
            print(f"{name.title()} - ${amount:.2f}")


def add_expense():
    details = get_expense_detail()

    if details is None:
        return None

    category, expense_name, expense_amount, due_date = details

    add_expense_core(category, expense_name, expense_amount, due_date)
    return None

def add_expense_core(category: Category, expense_name: str, expense_amount: float, due_date: datetime):
    """Handles the actual mutation of expenses dictionary"""
    expenses.setdefault(category, {})
    expenses[category][expense_name] = {
        'expense_amount': expense_amount,
        'due_date': due_date
    }


def delete_expense():
    """Helper function that facilitates calling and returning values"""
    returned = del_expense()

    if returned is None:
        return None

    category, name = returned

    del_expense_core(category, name)
    return None

def del_expense_core(category, didx):
    """Deletes expense from dictionary"""
    expenses[category].pop(didx, None)

    print(f"{didx} successfully deleted from {category}.")


def update_expense():
    category, former_expense, new_expense_name, new_expense_amount = edit_expense()
    new_expense_amount = float(new_expense_amount)

    update_expense_core(category, former_expense, new_expense_name, new_expense_amount)
    #values will update regardless of user input

    print(
        f"Updated expense: {new_expense_name} - ${new_expense_amount:.2f}"
    )

def update_expense_core(category, former_expense, new_expense, new_amount):
    """Deletes old expense, replaces it with updated expense"""

    expenses[category].pop(former_expense, None)
    #deletes old expense
    expenses[category][new_expense] = new_amount
