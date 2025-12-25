from expense import Expense
import json, os

class ExpenseTracker:
    def __init__(self, file_path="../data/expenses.json"):
        self.file_path = file_path
        self.expenses = self.load_expenses()

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
        self.save_expenses()
    
    def get_balance(self):
        pass

    def list_expenses(self, category=None):
        pass

    def save_expenses(self,):
        with open(self.file_path, "w") as f:
            json.dump(
                [e.__dict__ for e in self.expenses], 
                f,
                indent = 4 
             )
        
    def load_expenses(self):
        if not os.path.exists(self.file_path):
            return []
        
        if os.path.getsize(self.file_path) == 0:
            return []

        with open(self.file_path, "r") as f:
            data = json.load(f)

        return [Expense(**item) for item in data]
   
        