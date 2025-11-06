"""
Configure settings for expense due dates
"""

from datetime import date, timedelta

class BiweeklyExpense:
    ANCHOR_DATE = date.today()
    PERIOD_DAYS = 14
