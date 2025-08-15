import tkinter as tk
from tkinter import ttk, messagebox

# Stack class (DSA)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def get_all(self):
        return self.items

# Function to generate Fibonacci sequence using stack
def fibonacci(n):
    if n <= 0:
        return []
    stack = Stack()
    # First two Fibonacci numbers
    stack.push(0)
    if n > 1:
        stack.push(1)
    for i in range(2, n):
        a = stack.pop()
        b = stack.peek()
        stack.push(a)
        stack.push(a + b)
    return stack.get_all()

# Function triggered by button
def generate_sequence():
    try:
        n = int(entry.get())
        if n <= 0:
            messagebox.showwarning("Invalid Input", "Enter a positive integer.")
            return
        fib_sequence = fibonacci(n)
        result_label.config(text=f"Fibonacci Sequence ({n} terms):\n{fib_sequence}", foreground="green")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

# Reset input and result
def reset():
    entry.delete(0, tk.END)
    result_label.config(text="")

# GUI Setup
root = tk.Tk()
root.title("Fibonacci Sequence Generator")
root.geometry("500x400")
root.configure(bg="#f0f8ff")  # Light blue background

# Style (mimicking CSS)
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=8)
style.configure("TLabel", font=("Helvetica", 12), background="#f0f8ff")
style.configure("TEntry", font=("Helvetica", 14))

# Title
title_label = ttk.Label(root, text="Fibonacci Sequence Generator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=20)

# Entry for number of terms
entry = ttk.Entry(root, font=("Helvetica", 14), width=30)
entry.pack(pady=10)

# Generate button
generate_button = ttk.Button(root, text="Generate Sequence", command=generate_sequence)
generate_button.pack(pady=10)

# Result label
result_label = ttk.Label(root, text="", font=("Helvetica", 12), wraplength=450, justify="center")
result_label.pack(pady=20)

# Reset button
reset_button = ttk.Button(root, text="Reset", command=reset)
reset_button.pack(pady=10)

# Run the GUI
root.mainloop()
