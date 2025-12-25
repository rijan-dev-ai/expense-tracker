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


def main():
    parser = argparse.ArgumentParser("Expense Tracker CLI")
    subparser = parser.add_subparsers(dest="command")

    add_parser = subparser.add_parser("add")
    add_parser.add_argument("--amount", type=float, required=True)
    add_parser.add_argument("--category", required=True)
    add_parser.add_argument("--date", required=True)
    add_parser.add_argument("--description", default="")
    add_parser.add_argument("--type", choices=["income", "expense"], default="expense")
    add_parser.set_defaults(func=add_expense)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__=="__main__":
    main()
    

