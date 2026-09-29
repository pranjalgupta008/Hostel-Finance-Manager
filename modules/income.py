# ============================================
# HOSTEL FINANCE MANAGER
# Income Module
# ============================================

from utils.file_handler import save_transaction
def add_income():
    """Collect income details from the user."""

    print()
    print("=" * 50)
    print("                  ADD INCOME")
    print("=" * 50)

    # -------------------------------
    # 1. Select income source
    # -------------------------------

    print()
    print("Income Sources")
    print("-" * 30)

    print("1. Pocket Money")
    print("2. Scholarship")
    print("3. Part-time Work")
    print("4. Freelancing")
    print("5. Gift")
    print("6. Refund")
    print("7. Other")

    while True:

        source_choice = input("Select income source (1-7): ").strip()

        if source_choice.isdigit():

            source_choice = int(source_choice)

            if 1 <= source_choice <= 7:
                break

        print("❌ Invalid choice. Please enter a number from 1 to 7.")


    income_sources = {
        1: "Pocket Money",
        2: "Scholarship",
        3: "Part-time Work",
        4: "Freelancing",
        5: "Gift",
        6: "Refund",
        7: "Other"
    }

    source = income_sources[source_choice]


    # -------------------------------
    # 2. Description
    # -------------------------------

    while True:

        description = input("Enter description: ").strip()

        if description:
            break

        print("❌ Description cannot be empty.")


    # -------------------------------
    # 3. Enter amount
    # -------------------------------

    while True:

        amount_input = input("Enter amount received: ₹").strip()

        try:

            amount = float(amount_input)

            if amount > 0:
                break

            print("❌ Amount must be greater than zero.")

        except ValueError:

            print("❌ Please enter a valid number.")


    # -------------------------------
    # 4. Payment method
    # -------------------------------

    print()
    print("Payment Methods")
    print("-" * 30)

    print("1. UPI")
    print("2. Cash")
    print("3. Bank Transfer")
    print("4. Debit Card")
    print("5. Other")

    while True:

        payment_choice = input("Select payment method (1-5): ").strip()

        if payment_choice.isdigit():

            payment_choice = int(payment_choice)

            if 1 <= payment_choice <= 5:
                break

        print("❌ Invalid choice. Please enter a number from 1 to 5.")


    payment_methods = {
        1: "UPI",
        2: "Cash",
        3: "Bank Transfer",
        4: "Debit Card",
        5: "Other"
    }

    payment_method = payment_methods[payment_choice]


    # -------------------------------
    # 5. Display income information
    # -------------------------------

    print()
    print("=" * 50)
    print("              INCOME DETAILS")
    print("=" * 50)

    print(f"Source          : {source}")
    print(f"Description     : {description}")
    print(f"Amount          : ₹{amount:.2f}")
    print(f"Payment Method  : {payment_method}")

    print("=" * 50)
    print("✅ Income recorded successfully!")
    print("=" * 50)


    # -------------------------------
    # 6. Return income data
    # -------------------------------
    income_data = {
        "type": "Income",
        "source": source,
        "description": description,
        "amount": amount,
        "payment_method": payment_method
    }

    save_transaction(income_data)

    return income_data