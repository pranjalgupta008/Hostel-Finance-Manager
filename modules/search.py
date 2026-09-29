# ============================================
# HOSTEL FINANCE MANAGER
# Search Module
# ============================================

from utils.file_handler import load_transactions


def display_results(transactions):
    """Display a list of transactions."""

    if not transactions:

        print()
        print("=" * 70)
        print("                  SEARCH RESULTS")
        print("=" * 70)

        print()
        print("No matching transactions found.")

        print("=" * 70)

        return


    print()
    print("=" * 90)
    print("                         SEARCH RESULTS")
    print("=" * 90)

    print()

    print(
        f"{'No.':<5}"
        f"{'Type':<10}"
        f"{'Category':<18}"
        f"{'Description':<25}"
        f"{'Amount':>12}"
    )

    print("-" * 90)


    total = 0


    for number, transaction in enumerate(
        transactions,
        start=1
    ):

        transaction_type = transaction["Type"]

        category = transaction["Category"]

        source = transaction["Source"]

        description = transaction["Description"]

        amount = float(transaction["Amount"])


        # Show source for income
        if transaction_type == "Income":

            display_category = source

        else:

            display_category = category


        total += amount


        print(
            f"{number:<5}"
            f"{transaction_type:<10}"
            f"{display_category:<18}"
            f"{description:<25}"
            f"₹{amount:>10.2f}"
        )


    print("-" * 90)

    print(f"Total matching amount: ₹{total:.2f}")

    print("=" * 90)


def search_transactions():
    """Search transactions using different filters."""

    transactions = load_transactions()


    # Check for empty transaction list
    if not transactions:

        print()
        print("No transactions available to search.")

        return


    while True:

        print()
        print("=" * 50)
        print("            SEARCH TRANSACTIONS")
        print("=" * 50)

        print("1. Search by Type")
        print("2. Search by Category")
        print("3. Search by Payment Method")
        print("4. Search by Description")
        print("5. Search by Minimum Amount")
        print("6. View All Transactions")
        print("7. Back to Main Menu")

        print()


        choice = input(
            "Enter your choice: "
        ).strip()


        # -----------------------------------------
        # Search by Type
        # -----------------------------------------

        if choice == "1":

            print()
            print("1. Income")
            print("2. Expense")

            type_choice = input(
                "Select type: "
            ).strip()


            if type_choice == "1":

                results = [
                    transaction
                    for transaction in transactions
                    if transaction["Type"] == "Income"
                ]

            elif type_choice == "2":

                results = [
                    transaction
                    for transaction in transactions
                    if transaction["Type"] == "Expense"
                ]

            else:

                print("❌ Invalid choice.")

                continue


            display_results(results)


        # -----------------------------------------
        # Search by Category
        # -----------------------------------------

        elif choice == "2":

            category = input(
                "Enter category: "
            ).strip().lower()


            results = [
                transaction
                for transaction in transactions
                if transaction["Category"].lower()
                == category
            ]


            display_results(results)


        # -----------------------------------------
        # Search by Payment Method
        # -----------------------------------------

        elif choice == "3":

            payment_method = input(
                "Enter payment method: "
            ).strip().lower()


            results = [
                transaction
                for transaction in transactions
                if transaction["Payment Method"].lower()
                == payment_method
            ]


            display_results(results)


        # -----------------------------------------
        # Search by Description
        # -----------------------------------------

        elif choice == "4":

            keyword = input(
                "Enter description keyword: "
            ).strip().lower()


            results = [
                transaction
                for transaction in transactions
                if keyword
                in transaction["Description"].lower()
            ]


            display_results(results)


        # -----------------------------------------
        # Search by Minimum Amount
        # -----------------------------------------

        elif choice == "5":

            while True:

                amount_input = input(
                    "Enter minimum amount: ₹"
                ).strip()

                try:

                    minimum_amount = float(
                        amount_input
                    )

                    if minimum_amount >= 0:
                        break

                    print(
                        "❌ Amount cannot be negative."
                    )

                except ValueError:

                    print(
                        "❌ Please enter a valid number."
                    )


            results = [
                transaction
                for transaction in transactions
                if float(transaction["Amount"])
                >= minimum_amount
            ]


            display_results(results)


        # -----------------------------------------
        # View all transactions
        # -----------------------------------------

        elif choice == "6":

            display_results(transactions)


        # -----------------------------------------
        # Exit search menu
        # -----------------------------------------

        elif choice == "7":

            break


        else:

            print(
                "❌ Invalid choice. "
                "Please select 1-7."
            )