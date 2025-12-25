from expense import Expense
import json, os
from datetime import datetime

class ExpenseTracker:
    def __init__(self, file_path="../data/expenses.json"):
        self.file_path = file_path
        self.expenses = self.load_expenses()

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
        self.save_expenses()
    
    def get_balance(self):
        total_income = sum(e.amount for e in self.expenses if e.expense_type == "income")
        total_expense = sum(e.amount for e in self.expenses if e.expense_type == "expense")
        return total_income - total_expense

    def list_expenses(self, category=None, start_date = None, end_date = None):
        ''' 
        return list of expenses, optionally filtered by:
        - category
        - start_date and end_date (YYYY-MM-DD strings)
        '''
        filtered = self.expenses
        
        if category:
            filtered = [e for e in filtered if e.category.lower() == category.lower()]
        
        if start_date:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            filtered = [ e for e in filtered if datetime.strptime(e.date, "%Y-%m-%d") >= start]

        if end_date:
            end = datetime.strptime(end_date, "%Y-%m-%d")
            filtered = [ e for e in filtered if datetime.strptime(e.date, "%Y-%m-%d") <= end]

        return filtered

    def save_expenses(self,):
        ''' save all the expenses to JSON file'''
        # Ensure directory exists
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, "w") as f:
            json.dump(
                [e.to_dict() for e in self.expenses], 
                f,
                indent = 4 
             )
        
    def load_expenses(self):
        if not os.path.exists(self.file_path):
            return []
        
        if os.path.getsize(self.file_path) == 0:
            return []

        with open(self.file_path, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return []

        return [Expense(**item) for item in data]
   
        