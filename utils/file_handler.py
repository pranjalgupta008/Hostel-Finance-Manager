# ============================================
# HOSTEL FINANCE MANAGER
# File Handler Module
# ============================================
import csv
import os
from datetime import date

# Location of the transaction file
DATA_FOLDER = "data"
TRANSACTION_FILE = os.path.join(
    DATA_FOLDER,
    "transactions.csv"
)


def initialize_file():
    """
    Create the data folder and transaction file
    if they do not already exist.
    """

    # Create data folder
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    # Create CSV file if it does not exist
    if not os.path.exists(TRANSACTION_FILE):
        with open(
            TRANSACTION_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Date",
                "Type",
                "Category",
                "Subcategory",
                "Source",
                "Description",
                "Amount",
                "Payment Method"
            ])


def save_transaction(transaction):
    """
    Save one transaction into the CSV file.
    """

    initialize_file()

    with open(
        TRANSACTION_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if "date" not in transaction:
            transaction["date"] = str(date.today())
        writer.writerow([
            transaction.get("date", ""),
            transaction.get("type", ""),
            transaction.get("category", ""),
            transaction.get("subcategory", ""),
            transaction.get("source", ""),
            transaction.get("description", ""),
            transaction.get("amount", ""),
            transaction.get("payment_method", "")
        ])


def load_transactions():
    """
    Read all transactions from the CSV file.
    """

    initialize_file()

    transactions = []

    with open(
        TRANSACTION_FILE,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            transactions.append(row)

    return transactions