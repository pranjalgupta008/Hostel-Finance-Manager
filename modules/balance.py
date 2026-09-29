# ============================================
# HOSTEL FINANCE MANAGER
# Balance Module
# ============================================

from utils.file_handler import load_transactions


def get_financial_summary():
    """
    Calculate total income, total expenses,
    current balance and savings percentage.
    """

    transactions = load_transactions()

    total_income = 0
    total_expenses = 0

    # Go through every transaction
    for transaction in transactions:

        transaction_type = transaction["Type"]
        amount = float(transaction["Amount"])

        if transaction_type == "Income":

            total_income += amount

        elif transaction_type == "Expense":

            total_expenses += amount

    # Calculate balance
    balance = total_income - total_expenses

    # Calculate savings percentage
    if total_income > 0:

        savings_percentage = (
            balance / total_income
        ) * 100

    else:

        savings_percentage = 0

    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "balance": balance,
        "savings_percentage": savings_percentage
    }


def view_balance():
    """Display the student's financial summary."""

    summary = get_financial_summary()

    print()
    print("=" * 50)
    print("              FINANCIAL SUMMARY")
    print("=" * 50)

    print()

    print(
        f"Total Income       : "
        f"₹{summary['total_income']:.2f}"
    )

    print(
        f"Total Expenses     : "
        f"₹{summary['total_expenses']:.2f}"
    )

    print(
        f"Current Balance    : "
        f"₹{summary['balance']:.2f}"
    )

    print(
        f"Savings Percentage : "
        f"{summary['savings_percentage']:.2f}%"
    )

    print()
    print("=" * 50)