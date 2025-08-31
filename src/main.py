from enum import Enum, auto

class CATEGORY(Enum):
    AUTOMATIC=  auto()
    VARIABLE = auto()
    CREDIT_CARD = auto()
    ONE_TIME_EXPENSE = auto()

    def __str__(self):
        return self.name.replace("_"," ").title()

expenses = {}
