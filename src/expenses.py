"""Holds expenses dictionary, as well as Category enum class"""

from enum import StrEnum
from datetime import datetime
from typing import Dict, TypedDict


class Category(StrEnum):
    """A list of enumerated categories for expenses"""
    AUTOMATIC = "Automatic"
    VARIABLE = "Variable"
    CREDIT_CARD = "Credit Card"
    ONE_TIME_EXPENSE = "One Time Expense"


class ExpenseEntry(TypedDict):
    expense_amount: float
    due_date: datetime


ExpensesDict = Dict[Category, Dict[str, ExpenseEntry]]
## ALL core functions must follow this format
#ExpenseDict: a dictionary of a given Category,
#which is then a list containing a string value, and the values within ExpenseEntry
#(which would be the expense amount and its due date)

expenses: ExpensesDict = {cat: {} for cat in Category}
#the 'expenses' dictionary now follows a defined format,
#and will always load all four categories