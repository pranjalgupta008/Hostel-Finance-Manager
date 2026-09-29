# ============================================
# HOSTEL FINANCE MANAGER
# Expense Module
# ============================================

from utils.file_handler import save_transaction
def add_expense():
    """Collect expense details from the user."""


    # -----------------------------------------
    # 1. Heading
    # -----------------------------------------

    print()
    print("=" * 50)
    print("                 ADD EXPENSE")
    print("=" * 50)


    # -----------------------------------------
    # 2. Select main category
    # -----------------------------------------

    print()
    print("Expense Categories")
    print("-" * 30)

    print("1. Food")
    print("2. Education")
    print("3. Travel")
    print("4. Sports & Fitness")
    print("5. Entertainment")
    print("6. Personal")
    print("7. Hostel")
    print("8. Technology")
    print("9. Other")


    while True:

        category_choice = input(
            "Select expense category (1-9): "
        ).strip()

        if category_choice.isdigit():

            category_choice = int(category_choice)

            if 1 <= category_choice <= 9:
                break

        print("❌ Invalid choice. Please enter a number from 1 to 9.")


    categories = {
        1: "Food",
        2: "Education",
        3: "Travel",
        4: "Sports & Fitness",
        5: "Entertainment",
        6: "Personal",
        7: "Hostel",
        8: "Technology",
        9: "Other"
    }

    category = categories[category_choice]


    # -----------------------------------------
    # 3. Select subcategory
    # -----------------------------------------

    subcategories = {

        "Food": [
            "Mess",
            "Canteen",
            "Restaurant",
            "Snacks",
            "Tea/Coffee",
            "Vending Machine",
            "Food Delivery",
            "Other"
        ],

        "Education": [
            "Stationery",
            "Printouts",
            "Photocopy",
            "Books",
            "Lab Materials",
            "Project",
            "Other"
        ],

        "Travel": [
            "Bus",
            "Auto",
            "Cab",
            "Train",
            "Flight",
            "College Transport",
            "Other"
        ],

        "Sports & Fitness": [
            "Gym",
            "Sports Equipment",
            "Sports Event",
            "Other"
        ],

        "Entertainment": [
            "Movies",
            "Games",
            "Events",
            "Outing",
            "Other"
        ],

        "Personal": [
            "Clothing",
            "Toiletries",
            "Haircut",
            "Laundry",
            "Medicine",
            "Personal Care",
            "Other"
        ],

        "Hostel": [
            "Hostel Fee",
            "Room Supplies",
            "Maintenance",
            "Laundry",
            "Other"
        ],

        "Technology": [
            "Software",
            "Subscriptions",
            "Accessories",
            "Repairs",
            "Cloud Storage",
            "Other"
        ],

        "Other": [
            "Miscellaneous"
        ]
    }


    print()
    print(f"Subcategories for {category}")
    print("-" * 30)


    selected_subcategories = subcategories[category]


    for number, subcategory in enumerate(
        selected_subcategories,
        start=1
    ):
        print(f"{number}. {subcategory}")


    while True:

        subcategory_choice = input(
            f"Select subcategory (1-{len(selected_subcategories)}): "
        ).strip()

        if subcategory_choice.isdigit():

            subcategory_choice = int(subcategory_choice)

            if 1 <= subcategory_choice <= len(selected_subcategories):
                break

        print(
            f"❌ Invalid choice. "
            f"Please enter a number from 1 to {len(selected_subcategories)}."
        )


    subcategory = selected_subcategories[
        subcategory_choice - 1
    ]


    # -----------------------------------------
    # 4. Description
    # -----------------------------------------

    while True:

        description = input(
            "Enter expense description: "
        ).strip()

        if description:
            break

        print("❌ Description cannot be empty.")


    # -----------------------------------------
    # 5. Amount
    # -----------------------------------------

    while True:

        amount_input = input(
            "Enter expense amount: ₹"
        ).strip()

        try:

            amount = float(amount_input)

            if amount > 0:
                break

            print("❌ Amount must be greater than zero.")

        except ValueError:

            print("❌ Please enter a valid number.")


    # -----------------------------------------
    # 6. Payment method
    # -----------------------------------------

    print()
    print("Payment Methods")
    print("-" * 30)

    print("1. UPI")
    print("2. Cash")
    print("3. Debit Card")
    print("4. Credit Card")
    print("5. Bank Transfer")
    print("6. Other")


    while True:

        payment_choice = input(
            "Select payment method (1-6): "
        ).strip()

        if payment_choice.isdigit():

            payment_choice = int(payment_choice)

            if 1 <= payment_choice <= 6:
                break

        print("❌ Invalid choice. Please enter a number from 1 to 6.")


    payment_methods = {
        1: "UPI",
        2: "Cash",
        3: "Debit Card",
        4: "Credit Card",
        5: "Bank Transfer",
        6: "Other"
    }

    payment_method = payment_methods[payment_choice]


    # -----------------------------------------
    # 7. Display expense information
    # -----------------------------------------

    print()
    print("=" * 50)
    print("              EXPENSE DETAILS")
    print("=" * 50)

    print(f"Category        : {category}")
    print(f"Subcategory     : {subcategory}")
    print(f"Description     : {description}")
    print(f"Amount          : ₹{amount:.2f}")
    print(f"Payment Method  : {payment_method}")

    print("=" * 50)
    print("✅ Expense recorded successfully!")
    print("=" * 50)


    # -----------------------------------------
    # 8. Return expense data
    # -----------------------------------------
    
    expense_data = {
        "type": "Expense",
        "category": category,
        "subcategory": subcategory,
        "description": description,
        "amount": amount,
        "payment_method": payment_method
    }

    save_transaction(expense_data)

    return expense_data 