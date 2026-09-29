# ============================================
# HOSTEL FINANCE MANAGER
# Monthly Report Module
# ============================================

from utils.file_handler import load_transactions


def get_monthly_transactions(month, year):
    """Return transactions for a specific month and year."""

    transactions = load_transactions()

    monthly_transactions = []

    for transaction in transactions:

        date = transaction.get("Date", "")

        if not date:
            continue

        try:
            transaction_year = int(date[:4])
            transaction_month = int(date[5:7])

        except (ValueError, IndexError):
            continue

        if transaction_year == year and transaction_month == month:
            monthly_transactions.append(transaction)

    return monthly_transactions


def generate_monthly_report():
    """Generate a financial report for a selected month."""

    print()
    print("=" * 70)
    print("                     MONTHLY REPORT")
    print("=" * 70)

    # Month selection

    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    print()

    for number, name in months.items():
        print(f"{number:2}. {name}")

    print()

    while True:

        try:
            month = int(input("Enter month number: "))

            if 1 <= month <= 12:
                break

            print("Please enter a month between 1 and 12.")

        except ValueError:
            print("Please enter a valid number.")

    while True:

        try:
            year = int(input("Enter year: "))

            if 2000 <= year <= 2100:
                break

            print("Please enter a valid year.")

        except ValueError:
            print("Please enter a valid number.")

    # Get monthly transactions

    monthly_transactions = get_monthly_transactions(month, year)

    print()
    print("-" * 70)
    print(f"REPORT FOR {months[month].upper()} {year}")
    print("-" * 70)

    if not monthly_transactions:

        print()
        print("No transactions found for this month.")
        print("=" * 70)

        return

    # Financial calculations

    total_income = 0
    total_expenses = 0

    category_spending = {}

    for transaction in monthly_transactions:

        transaction_type = transaction.get("Type", "")

        amount = float(transaction.get("Amount", 0))

        if transaction_type == "Income":

            total_income += amount

        elif transaction_type == "Expense":

            total_expenses += amount

            category = transaction.get("Category", "Other")

            if category not in category_spending:
                category_spending[category] = 0

            category_spending[category] += amount

    balance = total_income - total_expenses

    if total_income > 0:
        savings_rate = (balance / total_income) * 100
    else:
        savings_rate = 0

    # Financial summary

    print()
    print("FINANCIAL SUMMARY")
    print("-" * 70)

    print(f"Total Income       : ₹{total_income:.2f}")
    print(f"Total Expenses     : ₹{total_expenses:.2f}")
    print(f"Monthly Balance    : ₹{balance:.2f}")
    print(f"Savings Rate       : {savings_rate:.2f}%")

    # Category breakdown

    print()
    print("EXPENSE BREAKDOWN")
    print("-" * 70)

    if category_spending:

        for category, amount in category_spending.items():

            print(f"{category:<25} ₹{amount:.2f}")

    else:

        print("No expenses recorded.")

    # Transaction count

    print()
    print("-" * 70)

    income_count = 0
    expense_count = 0

    for transaction in monthly_transactions:

        if transaction.get("Type") == "Income":
            income_count += 1

        elif transaction.get("Type") == "Expense":
            expense_count += 1

    print(f"Income Transactions : {income_count}")
    print(f"Expense Transactions: {expense_count}")

    print()
    print("=" * 70)