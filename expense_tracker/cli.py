import argparse
from expense import Expense
from tracker import ExpenseTracker

def add_expense(args):
    tracker = ExpenseTracker()
    expense = Expense(
        amount = args.amount,
        category = args.category,
        date = args.date,
        description = args.description,
        expense_type=args.type
    )
    tracker.add_expense(expense)
    print("Expense added successfully")


def list_expenses(args):
    tracker = ExpenseTracker()
    expenses = tracker.list_expenses(
        category=args.category,
        start_date=args.start_date,
        end_date = args.end_date
    )
    if not expenses:
        print("No expenses found")
        return
    
    print(f"{'Date':<12} {'Category':<15} {'Type':<10} {'Amount':<10} Description")
    print("-" * 60)
    for e in expenses:
        print(f"{e.date:<12} {e.category:<15} {e.expense_type:<10} {e.amount:<10} {e.description}")
    

def show_balance(args):
    tracker = ExpenseTracker()
    balance = tracker.get_balance()
    print(f"Current Balance: {balance}")

def main():
    parser = argparse.ArgumentParser("Expense Tracker CLI")
    subparser = parser.add_subparsers(dest="command")

    # ---- add command -----------
    add_parser = subparser.add_parser("add", help = "Add a new expense or income")
    add_parser.add_argument("--amount", type=float, required=True)
    add_parser.add_argument("--category", required=True)
    add_parser.add_argument("--date", required=True)
    add_parser.add_argument("--description", default="")
    add_parser.add_argument("--type", choices=["income", "expense"], default="expense")
    add_parser.set_defaults(func=add_expense)

    # ---- list command ----------
    list_parser = subparser.add_parser("list", help="List expenses")
    list_parser.add_argument("--category", help = "Filter by category")
    list_parser.add_argument("--start-date", help = "Start date YYYY-MM-DD")
    list_parser.add_argument("--end-date", help = "End date YYYY-MM-DD")
    list_parser.set_defaults(func=list_expenses)

    # ---- balance command --
    balance_parser = subparser.add_parser("balance", help="show current balance")
    balance_parser.set_defaults(func=show_balance)


    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__=="__main__":
    main()
    

