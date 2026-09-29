# ============================================
# HOSTEL FINANCE MANAGER
# Savings Module
# ============================================

import json
import os

from modules.balance import get_financial_summary


DATA_FOLDER = "data"
SAVINGS_FILE = os.path.join(
    DATA_FOLDER,
    "savings.json"
)


def initialize_savings_file():
    """Create the savings file if it does not exist."""

    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    if not os.path.exists(SAVINGS_FILE):

        with open(
            SAVINGS_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                {
                    "goal_name": "",
                    "goal_amount": 0
                },
                file,
                indent=4
            )


def load_savings_goal():
    """Load the current savings goal."""

    initialize_savings_file()

    with open(
        SAVINGS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_savings_goal(goal):
    """Save the savings goal."""

    initialize_savings_file()

    with open(
        SAVINGS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            goal,
            file,
            indent=4
        )


def set_savings_goal():
    """Allow the student to create or update a savings goal."""

    print()
    print("=" * 50)
    print("             SET SAVINGS GOAL")
    print("=" * 50)

    # Goal name
    while True:

        goal_name = input(
            "Enter your savings goal: "
        ).strip()

        if goal_name:
            break

        print("❌ Goal name cannot be empty.")

    # Goal amount
    while True:

        amount_input = input(
            "Enter target amount: ₹"
        ).strip()

        try:

            goal_amount = float(amount_input)

            if goal_amount > 0:
                break

            print("❌ Amount must be greater than zero.")

        except ValueError:

            print("❌ Please enter a valid number.")

    goal = {
        "goal_name": goal_name,
        "goal_amount": goal_amount
    }

    save_savings_goal(goal)

    print()
    print("=" * 50)
    print("             SAVINGS GOAL SAVED")
    print("=" * 50)

    print(f"Goal:       {goal_name}")
    print(f"Target:     ₹{goal_amount:.2f}")

    print("=" * 50)


def view_savings():
    """Display savings progress."""

    goal = load_savings_goal()

    summary = get_financial_summary()

    savings = summary["balance"]

    goal_name = goal["goal_name"]
    goal_amount = float(goal["goal_amount"])

    print()
    print("=" * 60)
    print("                 SAVINGS SUMMARY")
    print("=" * 60)

    print()
    print(f"Current Savings : ₹{savings:.2f}")

    # No goal set
    if not goal_name or goal_amount <= 0:

        print()
        print("No savings goal has been set.")

        print()
        print("Set a goal to start tracking your progress.")

        print("=" * 60)

        return

    print(f"Savings Goal    : {goal_name}")
    print(f"Target Amount   : ₹{goal_amount:.2f}")

    remaining = goal_amount - savings

    # Calculate progress
    progress = (
        savings / goal_amount
    ) * 100

    # Limit progress to 100%
    if progress > 100:
        progress = 100

    print(f"Progress        : {progress:.2f}%")

    print()

    if remaining > 0:

        print(
            f"Amount Remaining: "
            f"₹{remaining:.2f}"
        )

    else:

        print(
            "🎉 Savings goal reached!"
        )

        if remaining < 0:

            print(
                f"Extra savings: "
                f"₹{abs(remaining):.2f}"
            )

    print()
    print("=" * 60)