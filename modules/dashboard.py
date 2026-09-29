# ============================================
# HOSTEL FINANCE MANAGER
# Dashboard Module
# ============================================

from modules.balance import get_financial_summary
from modules.budget import load_budgets
from modules.savings import load_savings_goal
from modules.profile import load_profile
from modules.recurring import load_recurring_expenses
from utils.file_handler import load_transactions


def get_category_spending():
    """Calculate spending for each expense category."""

    transactions = load_transactions()

    spending = {}

    for transaction in transactions:

        if transaction["Type"] == "Expense":

            category = transaction["Category"]
            amount = float(transaction["Amount"])

            if category not in spending:
                spending[category] = 0

            spending[category] += amount

    return spending


def show_dashboard():
    """Display the complete financial dashboard."""

    # -----------------------------------------
    # Load all information
    # -----------------------------------------

    profile = load_profile()

    summary = get_financial_summary()

    budgets = load_budgets()

    savings_goal = load_savings_goal()

    recurring_expenses = load_recurring_expenses()

    spending = get_category_spending()


    # -----------------------------------------
    # Dashboard heading
    # -----------------------------------------

    print()
    print("=" * 70)
    print("                 FINANCIAL DASHBOARD")
    print("=" * 70)


    # -----------------------------------------
    # Student information
    # -----------------------------------------

    if profile:

        print()
        print(
            f"Welcome, {profile['name']}! 👋"
        )

        print(
            f"{profile['college']} | "
            f"{profile['course']} | "
            f"Year {profile['year']}"
        )

    else:

        print()
        print("Welcome to Hostel Finance Manager! 👋")

        print(
            "Student profile has not been created yet."
        )


    # -----------------------------------------
    # Financial overview
    # -----------------------------------------

    print()
    print("-" * 70)
    print("FINANCIAL OVERVIEW")
    print("-" * 70)

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
        f"Savings Rate       : "
        f"{summary['savings_percentage']:.2f}%"
    )


    # -----------------------------------------
    # Category spending
    # -----------------------------------------

    print()
    print("-" * 70)
    print("EXPENSE BREAKDOWN")
    print("-" * 70)

    if spending:

        for category, amount in spending.items():

            print(
                f"{category:<25}"
                f"₹{amount:.2f}"
            )

    else:

        print("No expenses recorded yet.")


    # -----------------------------------------
    # Budget status
    # -----------------------------------------

    print()
    print("-" * 70)
    print("BUDGET STATUS")
    print("-" * 70)

    if budgets:

        for category, budget in budgets.items():

            spent = spending.get(
                category,
                0
            )

            remaining = budget - spent

            if budget > 0:

                percentage = (
                    spent / budget
                ) * 100

            else:

                percentage = 0


            print(
                f"{category:<20}"
                f"₹{spent:.2f} / "
                f"₹{budget:.2f}"
                f"   ({percentage:.1f}%)"
            )

            if remaining < 0:

                print(
                    f"  🚨 Over budget by "
                    f"₹{abs(remaining):.2f}"
                )

            elif percentage >= 80:

                print(
                    "  ⚠️ Budget usage is high"
                )

    else:

        print("No budgets have been set.")


    # -----------------------------------------
    # Savings goal
    # -----------------------------------------

    print()
    print("-" * 70)
    print("SAVINGS GOAL")
    print("-" * 70)

    goal_name = savings_goal.get(
        "goal_name",
        ""
    )

    goal_amount = float(
        savings_goal.get(
            "goal_amount",
            0
        )
    )

    current_savings = summary["balance"]


    if goal_name and goal_amount > 0:

        progress = (
            current_savings / goal_amount
        ) * 100

        if progress > 100:
            progress = 100

        print(
            f"Goal             : {goal_name}"
        )

        print(
            f"Target           : "
            f"₹{goal_amount:.2f}"
        )

        print(
            f"Current Savings  : "
            f"₹{current_savings:.2f}"
        )

        print(
            f"Progress         : "
            f"{progress:.2f}%"
        )

    else:

        print("No savings goal has been set.")


    # -----------------------------------------
    # Recurring expenses
    # -----------------------------------------

    print()
    print("-" * 70)
    print("RECURRING EXPENSES")
    print("-" * 70)

    if recurring_expenses:

        total_recurring = 0

        for expense in recurring_expenses:

            amount = float(
                expense["amount"]
            )

            total_recurring += amount


        print(
            f"Active recurring expenses : "
            f"{len(recurring_expenses)}"
        )

        print(
            f"Total recurring amount    : "
            f"₹{total_recurring:.2f}"
        )

    else:

        print("No recurring expenses recorded.")


    # -----------------------------------------
    # End dashboard
    # -----------------------------------------

    print()
    print("=" * 70)