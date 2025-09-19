"""Holds expenses dictionary, as well as Category enum class"""

from enum import StrEnum


class Category(StrEnum):
    """A list of enumerated categories for expenses"""
    AUTOMATIC = "Automatic"
    VARIABLE = "Variable"
    CREDIT_CARD = "Credit Card"
    ONE_TIME_EXPENSE = "One Time Expense"


expenses: dict[Category, dict[str, float]] = {}
#expenses format: a dictionary of Categories, which is another dictionary of [str, float] formatted key:pairs
