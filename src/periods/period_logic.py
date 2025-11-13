"""
Business logic executed to correctly assign and track due dates
"""

from datetime import date, timedelta
from time import strftime
from src.periods.period_config import BiweeklyExpense
from src.expenses import expenses

def validate_due_date(exp_month, exp_day):
    """
    Validates a given expense date.
    """
    #may be added as its own code block rather than a function
    if exp_month and exp_day:
        formatted_date = strftime('%m,%d')
        return formatted_date
    return None

