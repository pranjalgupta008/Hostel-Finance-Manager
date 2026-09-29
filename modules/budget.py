# ============================================
# HOSTEL FINANCE MANAGER
# Budget Module
# ============================================

import json
import os

from utils.file_handler import load_transactions


# Location of budget file
DATA_FOLDER = "data"
BUDGET_FILE = os.path.join(
    DATA_FOLDER,
    "budgets.json"
)


def initialize_budget_file():
    """Create the budget file if it does not exist."""

    # Create data folder if necessary
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    # Create empty budget file
    if not os.path.exists(BUDGET_FILE):

        with open(
            BUDGET_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump({}, file, indent=4)


def load_budgets():
    """Load budgets from the JSON file."""

    initialize_budget_file()

    with open(
        BUDGET_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_budgets(budgets):
    """Save budgets to the JSON file."""

    initialize_budget_file()

    with open(
        BUDGET_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            budgets,
            file,
            indent=4
        )


def set_budget():
    """Allow the user to set or update a category budget."""

    print()
    print("=" * 50)
    print("               SET BUDGET")
    print("=" * 50)

    print()
    print("Budget Categories")
    print("-" * 30)

    categories = [
        "Food",
        "Education",
        "Travel",
        "Sports & Fitness",
        "Entertainment",
        "Personal",
        "Hostel",
        "Technology",
        "Other"
    ]

    for number, category in enumerate(
        categories,
        start=1
    ):
        print(f"{number}. {category}")

    # Select category
    while True:

        choice = input(
            "Select category (1-9): "
        ).strip()

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= 9:
                break

        print(
            "❌ Invalid choice. "
            "Please enter a number from 1 to 9."
        )

    category = categories[choice - 1]

    # Enter budget amount
    while True:

        amount_input = input(
            f"Enter monthly budget for {category}: ₹"
        ).strip()

        try:

            amount = float(amount_input)

            if amount > 0:
                break

            print("❌ Budget must be greater than zero.")

        except ValueError:

            print("❌ Please enter a valid number.")

    # Load existing budgets
    budgets = load_budgets()

    # Add/update budget
    budgets[category] = amount

    # Save budgets
    save_budgets(budgets)

    print()
    print("=" * 50)
    print("             BUDGET SAVED")
    print("=" * 50)

    print(f"Category : {category}")
    print(f"Budget   : ₹{amount:.2f}")

    print("=" * 50)


def view_budgets():
    """Display all budgets and current spending."""

    budgets = load_budgets()

    print()
    print("=" * 70)
    print("                    BUDGET STATUS")
    print("=" * 70)

    # No budgets
    if not budgets:

        print()
        print("No budgets have been set yet.")

        print("=" * 70)

        return

    # Load transactions
    transactions = load_transactions()

    # Store actual spending
    spending = {}

    for transaction in transactions:

        if transaction["Type"] == "Expense":

            category = transaction["Category"]

            amount = float(transaction["Amount"])

            if category not in spending:
                spending[category] = 0

            spending[category] += amount

    # Display budgets
    for category, budget in budgets.items():

        spent = spending.get(category, 0)

        remaining = budget - spent

        if budget > 0:

            percentage = (
                spent / budget
            ) * 100

        else:

            percentage = 0

        print()
        print(f"Category: {category}")
        print(f"Budget:   ₹{budget:.2f}")
        print(f"Spent:    ₹{spent:.2f}")
        print(f"Remaining: ₹{remaining:.2f}")
        print(f"Used:     {percentage:.2f}%")

        # Budget status
        if remaining < 0:

            print(
                f"🚨 OVER BUDGET by "
                f"₹{abs(remaining):.2f}"
            )

        elif percentage >= 80:

            print(
                "⚠️ WARNING: "
                "You have used 80% or more "
                "of this budget."
            )

        else:

            print("✅ Budget is under control.")

        print("-" * 50)