# ============================================
# HOSTEL FINANCE MANAGER
# Recurring Expense Module
# ============================================

import json
import os


DATA_FOLDER = "data"
RECURRING_FILE = os.path.join(
    DATA_FOLDER,
    "recurring_expenses.json"
)


def initialize_recurring_file():
    """Create the recurring expense file if needed."""

    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    if not os.path.exists(RECURRING_FILE):

        with open(
            RECURRING_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump([], file, indent=4)


def load_recurring_expenses():
    """Load recurring expenses."""

    initialize_recurring_file()

    with open(
        RECURRING_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_recurring_expenses(expenses):
    """Save recurring expenses."""

    initialize_recurring_file()

    with open(
        RECURRING_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            expenses,
            file,
            indent=4
        )


def add_recurring_expense():
    """Add a recurring expense."""

    print()
    print("=" * 55)
    print("             ADD RECURRING EXPENSE")
    print("=" * 55)

    # -----------------------------------------
    # Name
    # -----------------------------------------

    while True:

        name = input(
            "Enter expense name: "
        ).strip()

        if name:
            break

        print("❌ Name cannot be empty.")


    # -----------------------------------------
    # Amount
    # -----------------------------------------

    while True:

        amount_input = input(
            "Enter amount: ₹"
        ).strip()

        try:

            amount = float(amount_input)

            if amount > 0:
                break

            print("❌ Amount must be greater than zero.")

        except ValueError:

            print("❌ Please enter a valid number.")


    # -----------------------------------------
    # Frequency
    # -----------------------------------------

    print()
    print("Frequency")
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    print("4. Yearly")

    while True:

        frequency_choice = input(
            "Select frequency (1-4): "
        ).strip()

        if frequency_choice.isdigit():

            frequency_choice = int(
                frequency_choice
            )

            if 1 <= frequency_choice <= 4:
                break

        print("❌ Invalid choice. Enter 1-4.")


    frequencies = {
        1: "Daily",
        2: "Weekly",
        3: "Monthly",
        4: "Yearly"
    }

    frequency = frequencies[frequency_choice]


    # -----------------------------------------
    # Due date
    # -----------------------------------------

    while True:

        due_date = input(
            "Enter next due date (DD-MM-YYYY): "
        ).strip()

        if len(due_date) == 10:

            if (
                due_date[2] == "-"
                and due_date[5] == "-"
            ):
                break

        print(
            "❌ Invalid format. "
            "Use DD-MM-YYYY."
        )


    # -----------------------------------------
    # Save
    # -----------------------------------------

    expenses = load_recurring_expenses()

    new_expense = {
        "name": name,
        "amount": amount,
        "frequency": frequency,
        "next_due_date": due_date
    }

    expenses.append(new_expense)

    save_recurring_expenses(expenses)


    print()
    print("=" * 55)
    print("        RECURRING EXPENSE ADDED")
    print("=" * 55)

    print(f"Name:       {name}")
    print(f"Amount:     ₹{amount:.2f}")
    print(f"Frequency:  {frequency}")
    print(f"Next Due:   {due_date}")

    print("=" * 55)


def view_recurring_expenses():
    """Display all recurring expenses."""

    expenses = load_recurring_expenses()

    print()
    print("=" * 75)
    print("                 RECURRING EXPENSES")
    print("=" * 75)

    if not expenses:

        print()
        print("No recurring expenses found.")

        print("=" * 75)

        return


    print()

    print(
        f"{'No.':<5}"
        f"{'Name':<25}"
        f"{'Amount':>12}"
        f"{'Frequency':<15}"
        f"{'Next Due':<15}"
    )

    print("-" * 75)


    total = 0


    for number, expense in enumerate(
        expenses,
        start=1
    ):

        name = expense["name"]

        amount = float(expense["amount"])

        frequency = expense["frequency"]

        due_date = expense["next_due_date"]

        total += amount


        print(
            f"{number:<5}"
            f"{name:<25}"
            f"₹{amount:>10.2f}"
            f"{frequency:<15}"
            f"{due_date:<15}"
        )


    print("-" * 75)

    print(
        f"Total recurring amount: ₹{total:.2f}"
    )

    print("=" * 75)


def delete_recurring_expense():
    """Delete a recurring expense."""

    expenses = load_recurring_expenses()

    if not expenses:

        print()
        print("No recurring expenses to delete.")

        return


    view_recurring_expenses()

    print()

    while True:

        choice = input(
            "Enter expense number to delete: "
        ).strip()

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(expenses):
                break

        print(
            "❌ Invalid expense number."
        )


    removed = expenses.pop(choice - 1)

    save_recurring_expenses(expenses)


    print()
    print(
        f"✅ '{removed['name']}' "
        f"was removed successfully."
    )


def recurring_expense_menu():
    """Display the recurring expense menu."""

    while True:

        print()
        print("=" * 55)
        print("          RECURRING EXPENSE MANAGEMENT")
        print("=" * 55)

        print("1. Add Recurring Expense")
        print("2. View Recurring Expenses")
        print("3. Delete Recurring Expense")
        print("4. Back to Main Menu")

        print()

        choice = input(
            "Enter your choice: "
        ).strip()


        if choice == "1":

            add_recurring_expense()


        elif choice == "2":

            view_recurring_expenses()


        elif choice == "3":

            delete_recurring_expense()


        elif choice == "4":

            break


        else:

            print(
                "❌ Invalid choice. "
                "Please select 1-4."
            )