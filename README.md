# Hostel Finance Manager

## Overview

**Hostel Finance Manager** is a Python-based personal finance management application designed for college students living in hostels.

Managing money as a college student can become difficult when expenses come from different areas such as food, education, travel, entertainment, hostel requirements, technology, and personal needs. Keeping track of these expenses manually can make it difficult to understand spending patterns, available balance, budgets, and savings.

The Hostel Finance Manager provides a structured solution for recording and managing student financial information through a simple menu-driven console application.

The application allows users to:

- Record income
- Record expenses
- View financial transactions
- Calculate total income, expenses, and balance
- Set and monitor category-wise budgets
- Create and track savings goals
- Generate monthly financial reports
- Search transactions
- Manage recurring expenses
- Maintain a student profile
- View a consolidated financial dashboard

The project is developed using a modular Python structure where different functionalities are separated into individual modules. Financial transaction data is stored using CSV files, while other application information is stored using JSON files.

---

## Features

### 1. Income Management

The application allows students to record different sources of income, including:

- Pocket Money
- Scholarship
- Part-time Work
- Freelancing
- Gift
- Refund
- Other

Each income transaction stores information such as the source, description, amount, and payment method.

---

### 2. Expense Management

Students can record their expenses using different categories:

- Food
- Education
- Travel
- Sports & Fitness
- Entertainment
- Personal
- Hostel
- Technology
- Other

The application also provides subcategories for detailed expense classification.

For example, Food expenses can be categorized into:

- Mess
- Canteen
- Restaurant
- Snacks
- Tea/Coffee
- Vending Machine
- Food Delivery
- Other

Different payment methods can also be recorded for expenses.

---

### 3. Transaction Management

The application stores and displays financial transactions.

Users can view:

- Date
- Transaction Type
- Category
- Description
- Amount

The system also calculates:

- Total Income
- Total Expenses
- Current Balance

---

### 4. Balance Management

The application automatically calculates the student's current financial balance from recorded transactions.

The basic calculation is:

**Balance = Total Income − Total Expenses**

The balance module also provides a savings percentage based on the financial summary.

---

### 5. Budget Management

Students can create and manage category-wise budgets.

The budget module allows users to:

- Set a budget
- Update a budget
- View budget status
- Compare spending against the budget

The system provides a warning when spending reaches a high percentage of the allocated budget and an alert when the budget is exceeded.

---

### 6. Savings Management

The savings module allows students to create a savings goal.

Users can define:

- Savings goal name
- Target amount

The application calculates current savings using the current financial balance and displays the progress toward the savings target.

---

### 7. Monthly Financial Report

The monthly report module allows users to generate a financial report for a selected month and year.

The report includes:

- Total income
- Total expenses
- Monthly balance
- Savings rate
- Category-wise spending
- Number of income transactions
- Number of expense transactions

---

### 8. Transaction Search

Users can search financial transactions using different criteria:

- Transaction Type
- Category
- Payment Method
- Description Keyword
- Minimum Amount
- View All Transactions

This allows users to quickly locate specific financial records.

---

### 9. Recurring Expense Management

The recurring expense module allows students to maintain a list of regular expenses.

Users can:

- Add recurring expenses
- View recurring expenses
- Delete recurring expenses

Supported frequencies are:

- Daily
- Weekly
- Monthly
- Yearly

A due date can also be specified for recurring expenses.

---

### 10. Student Profile

The application allows students to maintain a basic profile containing:

- Student Name
- College
- Course
- Year
- Hostel
- Room Number
- Monthly Allowance

The profile information is also used in the financial dashboard.

---

### 11. Financial Dashboard

The dashboard provides a consolidated view of the student's financial information.

It can display:

- Student profile
- Total income
- Total expenses
- Current balance
- Expense breakdown by category
- Budget status
- Savings goal
- Recurring expenses

This allows important financial information to be viewed from one place.

---

## Main Menu

The application provides the following main menu:

```text
1. Add Income
2. Add Expense
3. View Transactions
4. View Balance
5. Manage Budget
6. Savings Management
7. Monthly Report
8. Search Transactions
9. Recurring Expenses
10. Student Profile
11. Financial Dashboard
12. Exit