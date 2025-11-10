"""
Configure settings for expense due dates
"""

from datetime import date

class BiweeklyExpense:
    """
    Establishes fixed anchor dates and period days
    """
    #ANCHOR_DATE is fixed to the system date for now, but will be
    #eventually tied to the last payday
    ANCHOR_DATE = date.today()
    PERIOD_DAYS = 14
