# # Stack class (DSA)
# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         return None

#     def is_empty(self):
#         return len(self.items) == 0

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         return None

# # Palindrome Checker Function
# def is_palindrome(word):
#     stack = Stack()
#     # Push all characters to stack
#     for char in word:
#         stack.push(char)
    
#     reversed_word = ''
#     # Pop characters from stack to create reversed string
#     while not stack.is_empty():
#         reversed_word += stack.pop()
    
#     return word == reversed_word

# # User Input
# word = input("Enter a word or phrase: ").replace(" ", "").lower()

# # Check if palindrome
# if is_palindrome(word):
#     print(f"'{word}' is a palindrome!")
# else:
#     print(f"'{word}' is not a palindrome!")



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

    def is_empty(self):
        return len(self.items) == 0

# Function to check palindrome
def check_palindrome():
    word = entry.get().replace(" ", "").lower()
    stack = Stack()
    
    # Push all characters to stack
    for char in word:
        stack.push(char)
    
    reversed_word = ''
    while not stack.is_empty():
        reversed_word += stack.pop()
    
    if word == reversed_word:
        result_label.config(text=f"'{entry.get()}' is a palindrome!", foreground="green")
    else:
        result_label.config(text=f"'{entry.get()}' is not a palindrome!", foreground="red")

# GUI Setup
root = tk.Tk()
root.title("Palindrome Checker")
root.geometry("450x300")
root.configure(bg="#f0f8ff")  # Light blue background

# Style
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=8)
style.configure("TLabel", font=("Helvetica", 12), background="#f0f8ff")

# Title
title_label = ttk.Label(root, text="Palindrome Checker", font=("Helvetica", 16, "bold"))
title_label.pack(pady=20)

# Entry box
entry = ttk.Entry(root, font=("Helvetica", 14), width=30)
entry.pack(pady=10)

# Check button
check_button = ttk.Button(root, text="Check", command=check_palindrome)
check_button.pack(pady=10)

# Result label
result_label = ttk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

# Reset button
def reset():
    entry.delete(0, tk.END)
    result_label.config(text="")

reset_button = ttk.Button(root, text="Reset", command=reset)
reset_button.pack(pady=10)

# Run the GUI
root.mainloop()
