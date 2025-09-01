'''Take user input to return as parameters to pass through business logic'''

from enum import Enum, auto
class CATEGORY(Enum):
    '''A list of enumerated categories for expenses'''
    AUTOMATIC=  auto()
    VARIABLE = auto()
    CREDIT_CARD = auto()
    ONE_TIME_EXPENSE = auto()

    def __str__(self):
        return self.name.replace("_"," ").title()

def get_expense_detail():
    '''Collects and returns expense details.
    Parameters:
        Category (represented by category index, or 'cidx'), must be entered as a number to be converted back to an integer
        Expense name (represented by a string)
        Expense amount (represented by an integer)
    '''
    for i, cat in enumerate(CATEGORY, 1):
        print(f"{i}. {cat}")

    print("Enter the category number for this expense.")
    cidx = int(input("> "))

    try:
        cidx = CATEGORY(cidx - 1)
    except ValueError:
        print("Invalid entry. Please enter the corresponding number.")
        return get_expense_detail

    print("Enter the expense name.")
    expense_name = str(input("> "))

    print("Enter expense amount.")
    while True:
        try:
            expense_amount = float(input("> $"))
        except ValueError:
            print("Invalid. Use only numbers and decimals.")
            continue
        break

    print(f"Expense: {expense_name}, {expense_amount}, in {cidx}.")
    print("Confirm expense? (y/n)")
    confirm = str(input("> "))

    if confirm == 'y':
        return cidx, expense_name, expense_amount
    elif confirm == 'n':
        return None
    else:
        print("Invalid entry. Please enter 'y' or 'n'.")
        return None

get_expense_detail()