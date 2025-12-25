class Expense:
    def __init__(self, amount: float, category: str, date: str, expense_type: str, description: str = ""):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
        self.expense_type = expense_type