import json
import os

# --- CONFIGURATION ---
DATA_FILE = "finance_data.json"

def load_data():
    """Loads data from the JSON file. If file doesn't exist, returns an empty list."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def save_data(transactions):
    """Saves the transaction list to the JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(transactions, file, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")

def add_transaction(transactions):
    """Prompts user for input and adds a new record."""
    print("\n--- Add New Transaction ---")
    t_type = input("Is this an (I)ncome or (E)xpense? ").strip().lower()
    
    if t_type == 'i':
        category_type = "Income"
    elif t_type == 'e':
        category_type = "Expense"
    else:
        print("Invalid choice. Returning to menu.")
        return

    try:
        amount = float(input("Enter the amount: "))
        category = input("Enter category (e.g., Food, Salary, Rent): ").capitalize()
        
        entry = {
            "type": category_type,
            "amount": amount,
            "category": category
        }
        
        transactions.append(entry)
        save_data(transactions)
        print(f"Successfully added {category_type}!")
    except ValueError:
        print("Invalid amount! Please enter a numeric value.")

def view_summary(transactions):
    """Calculates totals and displays them clearly."""
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'Income')
    total_expense = sum(t['amount'] for t in transactions if t['type'] == 'Expense')
    balance = total_income - total_expense

    print("\n" + "="*30)
    print(f"{'FINANCIAL SUMMARY':^30}")
    print("="*30)
    print(f"Total Income:   PKR {total_income:,.2f}")
    print(f"Total Expenses: PKR {total_expense:,.2f}")
    print("-" * 30)
    print(f"Current Balance: PKR {balance:,.2f}")
    print("="*30)

def main():
    """The main program loop."""
    transactions = load_data()
    
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Transaction")
        print("2. View Summary & Balance")
        print("3. View Transaction History")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_summary(transactions)
        elif choice == "3":
            print("\n--- History ---")
            for i, t in enumerate(transactions, 1):
                print(f"{i}. {t['type']}: PKR{t['amount']} ({t['category']})")
        elif choice == "4":
            print("KESA LAGA MERA MAZAK!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
