# ============================================
# HOSTEL FINANCE MANAGER
# Main Program
# ============================================

from modules.income import add_income
from modules.expense import add_expense 
from modules.transactions import view_transactions
from modules.balance import view_balance
from modules.budget import set_budget, view_budgets
from modules.savings import set_savings_goal, view_savings
from modules.search import search_transactions
from modules.recurring import recurring_expense_menu
from modules.profile import profile_menu
from modules.dashboard import show_dashboard
from modules.monthly_report import generate_monthly_report
def show_header():
    """Display the application header."""

    print()
    print("=" * 50)
    print("           HOSTEL FINANCE MANAGER")
    print("=" * 50)


def show_menu():
    """Display the main menu."""

    print()
    print("1.  Add Income")
    print("2.  Add Expense")
    print("3.  View Transactions")
    print("4.  View Balance")
    print("5.  Manage Budget")
    print("6.  View Savings")
    print("7.  Monthly Report")
    print("8.  Search Transactions")
    print("9.  Recurring Expenses")
    print("10. Student Profile")
    print("11. Financial Dashboard")
    print("12. Exit")
    print("-" * 50)


def get_choice():
    """Get and validate the user's menu choice."""

    while True:

        choice = input("Enter your choice: ").strip()

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= 12:
                return choice

        print("❌ Invalid choice.")
        print("Please enter a number between 1 and 12.")






def monthly_report():
    """Temporary function for generating monthly reports."""

    print()
    print("-" * 50)
    print("              MONTHLY REPORT")
    print("-" * 50)

    print("Report module will be connected here.")



def main():
    """Main controller of the application."""

    while True:

        show_header()
        show_menu()

        choice = get_choice()

        if choice == 1:
            add_income()

        elif choice == 2:
            add_expense()

        elif choice == 3:
            view_transactions()

        elif choice == 4:
            view_balance()

        elif choice == 5:
            while True:
                print()
                print("=" * 50)
                print("              BUDGET MANAGEMENT")
                print("=" * 50)

                print("1. Set / Update Budget")
                print("2. View Budget Status")
                print("3. Back to Main Menu")

                budget_choice = input("Enter your choice: ").strip()

                if budget_choice == "1":
                    set_budget()
                elif budget_choice == "2":
                    view_budgets()
                elif budget_choice == "3":
                    break
                else:
                    print("❌ Invalid choice.")
                    print("Please enter a number between 1 and 3.")

        elif choice == 6:
            while True:
                print()
                print("=" * 50)
                print("             SAVINGS MANAGEMENT")
                print("=" * 50)

                print("1. Set / Update Savings Goal")
                print("2. View Savings Progress")
                print("3. Back to Main Menu")

                savings_choice = input("Enter your choice: ").strip()

                if savings_choice == "1":
                    set_savings_goal()
                elif savings_choice == "2":
                    view_savings()
                elif savings_choice == "3":
                    break
                else:
                    print("❌ Invalid choice. Please enter 1, 2 or 3.")


        elif choice == 7:
            generate_monthly_report()

        elif choice == 8:
            search_transactions()

        elif choice == 9:
            recurring_expense_menu()

        elif choice == 10:
            profile_menu()

        elif choice == 11:
            show_dashboard()

        elif choice == 12:

            print()
            print("=" * 50)
            print("Thank you for using Hostel Finance Manager!")
            print("Goodbye 👋")
            print("=" * 50)

            break


# Start the application
if __name__ == "__main__":
    main()