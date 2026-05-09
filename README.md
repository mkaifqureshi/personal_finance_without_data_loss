Personal Finance Tracker (Python)
A lightweight, console-based financial management application built with Python. This tool allows users to track their incomes and expenses, visualize their current balance in PKR, and maintain a persistent record of all transactions using JSON storage.

🚀 Features
Persistent Storage: Uses JSON file handling to ensure your financial data is saved and reloaded every time you run the app.

PKR Currency Formatting: Built-in support for Pakistani Rupee formatting, including thousands-separators (e.g., 50,000.00 PKR).

Object-Oriented Programming (OOP): Built using Python classes for better code organization and scalability.

Real-time Summary: Automatically calculates total income, total expenses, and the remaining net balance.

Input Validation: Robust error handling to prevent the program from crashing on invalid numeric inputs.

🛠️ Concepts Learned
By building this project, I practiced the following Python skills:

File I/O: Reading from and writing to .json files.

Classes & Objects: Using __init__ and class methods to manage state.

List Comprehension: Efficiently filtering and summing data in a single line.

Error Handling: Implementing try...except blocks for user input.

String Formatting: Using f-strings with precision and comma separators.

📋 How to Run
Ensure you have Python 3.x installed.

Download finance_tracker.py.

Run the script via terminal/command prompt:

Bash
python finance_tracker.py
📸 Preview
Plaintext
======= PKR FINANCE MANAGER =======
1. Add Income/Expense
2. View Balance Sheet
3. Transaction History
4. Exit
Select an option: 2

------------------------------
Total Income:   PKR 75,000.00
Total Expenses: PKR 12,500.00
Current Balance: PKR 62,500.00
------------------------------
