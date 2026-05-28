Expense Tracker

A modular command-line based Expense Tracker application built using Python and SQLite.
This project allows users to manage daily expenses efficiently with features like CRUD operations, analytics, searching, sorting, exporting, and database backup.

Features
Expense Management
Add new expenses
View all expenses
Update existing expenses
Delete single expense
Delete all expense

Technologies Used
Technology	Purpose
Python	Main programming language
SQLite3	Database management
CSV Module	Export functionality
Datetime	Date validation
Shutil	Database backup

Project Structure
Expense Tracker/
│
├── main.py
├── database.py
├── analytics.py
├── utils.py
├── expenses.db
├── exported_expenses.csv
└── README.md

How to Run the Project
1. Clone Repository
git clone <your-repository-link>
2. Open Project Folder
cd ExpenseTracker
3. Run Program
python main.py