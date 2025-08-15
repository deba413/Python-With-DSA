import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# DSA List to store transactions
transactions = []  # Each transaction is a dictionary

# Functions
def add_income():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get().strip()
        date_str = date_entry.get().strip() or datetime.today().strftime("%Y-%m-%d")
        datetime.strptime(date_str, "%Y-%m-%d")
        transactions.append({"type": "Income", "amount": amount, "category": category, "date": date_str})
        display_transactions()
        reset_fields()
    except ValueError:
        messagebox.showwarning("Error", "Enter valid amount and date (YYYY-MM-DD)!")

def add_expense():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get().strip()
        date_str = date_entry.get().strip() or datetime.today().strftime("%Y-%m-%d")
        datetime.strptime(date_str, "%Y-%m-%d")
        transactions.append({"type": "Expense", "amount": amount, "category": category, "date": date_str})
        display_transactions()
        reset_fields()
    except ValueError:
        messagebox.showwarning("Error", "Enter valid amount and date (YYYY-MM-DD)!")

def display_transactions():
    transaction_listbox.delete(0, tk.END)
    income_total = sum(t["amount"] for t in transactions if t["type"] == "Income")
    expense_total = sum(t["amount"] for t in transactions if t["type"] == "Expense")
    balance = income_total - expense_total
    total_label.config(text=f"Income: ₹{income_total} | Expenses: ₹{expense_total} | Balance: ₹{balance}")

    for t in transactions:
        transaction_listbox.insert(tk.END, f"{t['date']} | {t['type']} | {t['category']} | ₹{t['amount']}")

def reset_fields():
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Budget Tracker")
root.geometry("700x500")
root.configure(bg="#f0f8ff")  # Light blue background

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=6)
style.configure("TLabel", font=("Helvetica", 12), background="#f0f8ff")
style.configure("TEntry", font=("Helvetica", 12))

# Title
ttk.Label(root, text="Simple Budget Tracker", font=("Helvetica", 16, "bold")).pack(pady=10)

# Input Frame
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

ttk.Label(input_frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
amount_entry = ttk.Entry(input_frame, width=15)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Category:").grid(row=0, column=2, padx=5, pady=5)
category_entry = ttk.Entry(input_frame, width=20)
category_entry.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(input_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=4, padx=5, pady=5)
date_entry = ttk.Entry(input_frame, width=15)
date_entry.grid(row=0, column=5, padx=5, pady=5)

# Buttons Frame
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)
ttk.Button(button_frame, text="Add Income", command=add_income).grid(row=0, column=0, padx=5)
ttk.Button(button_frame, text="Add Expense", command=add_expense).grid(row=0, column=1, padx=5)
ttk.Button(button_frame, text="Reset Fields", command=reset_fields).grid(row=0, column=2, padx=5)

# Transaction Listbox
transaction_listbox = tk.Listbox(root, width=95, height=20, font=("Helvetica", 12))
transaction_listbox.pack(pady=10)

# Total Label
total_label = ttk.Label(root, text="Income: ₹0 | Expenses: ₹0 | Balance: ₹0", font=("Helvetica", 14, "bold"))
total_label.pack(pady=10)

# Run GUI
root.mainloop()
