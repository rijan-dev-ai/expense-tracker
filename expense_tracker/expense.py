class Expense:
    def __init__(self, amount: float, category: str, date: str, expense_type: str, description: str = ""):
        self.amount = amount
        self.category = category
        self.date = date
        self.expense_type = expense_type
        self.description = description
       
    def to_dict(self,):
        return {
            "amount":self.amount,
            "category":self.category,
            "date":self.date,
            "expense_type":self.expense_type,
            "description":self.description
        }