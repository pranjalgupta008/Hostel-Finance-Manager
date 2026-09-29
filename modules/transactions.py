# ============================================
# HOSTEL FINANCE MANAGER
# Transaction Module
# ============================================

from utils.file_handler import load_transactions


def view_transactions():
    """Display all saved transactions."""

    # Load transactions from CSV file
    transactions = load_transactions()

    # Check if there are no transactions
    if not transactions:

        print()
        print("=" * 60)
        print("                 TRANSACTIONS")
        print("=" * 60)

        print()
        print("No transactions found.")

        print("=" * 60)

        return

    # Heading
    print()
    print("=" * 80)
    print("                         ALL TRANSACTIONS")
    print("=" * 80)

    print()

    # Table heading
    print(
        f"{'No.':<5}"
        f"{'Date':<12}"
        f"{'Type':<10}"
        f"{'Category':<18}"
        f"{'Description':<25}"
        f"{'Amount':>12}"
    )

    print("-" * 80)

    # Variables for calculations
    total_income = 0
    total_expenses = 0

    # Display every transaction
    for number, transaction in enumerate(
        transactions,
        start=1
    ):

        transaction_type = transaction["Type"]

        category = transaction["Category"]

        source = transaction["Source"]

        description = transaction["Description"]
        date = transaction.get("Date", "N/A")
        amount = float(transaction["Amount"])

        # Income transaction
        if transaction_type == "Income":

            display_category = source

            total_income += amount

        # Expense transaction
        else:

            display_category = category

            total_expenses += amount

        # Display transaction
        print(
            f"{number:<5}"
            f"{date:<12}"
            f"{transaction_type:<12}"
            f"{display_category:<20}"
            f"{description:<25}"
            f"₹{amount:>11.2f}"
        )

    # Calculate balance
    balance = total_income - total_expenses

    # Display financial summary
    print("-" * 80)

    print()
    print("FINANCIAL SUMMARY")
    print("-" * 40)

    print(f"Total Income     : ₹{total_income:.2f}")
    print(f"Total Expenses   : ₹{total_expenses:.2f}")
    print(f"Current Balance  : ₹{balance:.2f}")

    print("-" * 40)