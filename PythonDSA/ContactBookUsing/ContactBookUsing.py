import tkinter as tk
from tkinter import ttk, messagebox

# Stack class for DSA (to keep track of operations)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def get_all(self):
        return self.items

# Contact Book Class
class ContactBook:
    def __init__(self):
        self.contacts = {}  # Dictionary to store contacts
        self.history = Stack()  # Stack to keep operation history (DSA)

    def add_contact(self, name, number):
        if name in self.contacts:
            return False
        self.contacts[name] = number
        self.history.push(f"Added: {name}")
        return True

    def update_contact(self, name, number):
        if name in self.contacts:
            self.contacts[name] = number
            self.history.push(f"Updated: {name}")
            return True
        return False

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.history.push(f"Deleted: {name}")
            return True
        return False

    def search_contact(self, name):
        return self.contacts.get(name, None)

    def get_all_contacts(self):
        return self.contacts

# GUI Functions
def add_contact_gui():
    name = name_entry.get().strip()
    number = number_entry.get().strip()
    if not name or not number:
        messagebox.showwarning("Input Error", "Enter both name and number")
        return
    if book.add_contact(name, number):
        messagebox.showinfo("Success", f"Contact '{name}' added!")
        display_contacts()
    else:
        messagebox.showwarning("Error", "Contact already exists!")

def update_contact_gui():
    name = name_entry.get().strip()
    number = number_entry.get().strip()
    if book.update_contact(name, number):
        messagebox.showinfo("Success", f"Contact '{name}' updated!")
        display_contacts()
    else:
        messagebox.showwarning("Error", "Contact not found!")

def delete_contact_gui():
    name = name_entry.get().strip()
    if book.delete_contact(name):
        messagebox.showinfo("Success", f"Contact '{name}' deleted!")
        display_contacts()
    else:
        messagebox.showwarning("Error", "Contact not found!")

def search_contact_gui():
    name = name_entry.get().strip()
    number = book.search_contact(name)
    if number:
        messagebox.showinfo("Found", f"{name}: {number}")
    else:
        messagebox.showwarning("Not Found", f"Contact '{name}' does not exist.")

def display_contacts():
    contacts_text.config(state="normal")
    contacts_text.delete(1.0, tk.END)
    for name, number in book.get_all_contacts().items():
        contacts_text.insert(tk.END, f"{name} : {number}\n")
    contacts_text.config(state="disabled")

def reset_fields():
    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)

# Initialize Contact Book
book = ContactBook()

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("600x500")
root.configure(bg="#f0f8ff")  # Light blue background

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=6)
style.configure("TLabel", font=("Helvetica", 12), background="#f0f8ff")
style.configure("TEntry", font=("Helvetica", 12))

# Title
title_label = ttk.Label(root, text="Contact Book", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Name & Number Entries
frame = ttk.Frame(root)
frame.pack(pady=10)

ttk.Label(frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = ttk.Entry(frame, width=25)
name_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Number:").grid(row=1, column=0, padx=5, pady=5)
number_entry = ttk.Entry(frame, width=25)
number_entry.grid(row=1, column=1, padx=5, pady=5)

# Buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Add Contact", command=add_contact_gui).grid(row=0, column=0, padx=5)
ttk.Button(button_frame, text="Update Contact", command=update_contact_gui).grid(row=0, column=1, padx=5)
ttk.Button(button_frame, text="Delete Contact", command=delete_contact_gui).grid(row=0, column=2, padx=5)
ttk.Button(button_frame, text="Search Contact", command=search_contact_gui).grid(row=0, column=3, padx=5)
ttk.Button(button_frame, text="Reset Fields", command=reset_fields).grid(row=0, column=4, padx=5)

# Display Contacts
contacts_text = tk.Text(root, height=15, width=60, state="disabled", font=("Helvetica", 12))
contacts_text.pack(pady=10)

# Run GUI
root.mainloop()
