import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Cart as DSA List
cart = []

# Functions
def add_item():
    name = name_entry.get().strip()
    price = price_entry.get().strip()
    quantity = quantity_entry.get().strip()
    date = date_entry.get().strip()

    if not name or not price or not quantity or not date:
        messagebox.showwarning("Input Error", "Fill all fields!")
        return

    try:
        price = float(price)
        quantity = int(quantity)
        datetime.strptime(date, "%Y-%m-%d")  # Validate date format
    except ValueError:
        messagebox.showwarning("Input Error", "Enter valid price, quantity, and date (YYYY-MM-DD)!")
        return

    # Check if item already exists in cart
    for item in cart:
        if item["name"] == name and item["date"] == date:
            item["quantity"] += quantity
            item["price"] = price  # Update price if changed
            display_cart()
            reset_fields()
            return

    # Add new item
    cart.append({"name": name, "price": price, "quantity": quantity, "date": date})
    display_cart()
    reset_fields()

def remove_item():
    selected = cart_listbox.curselection()
    if selected:
        index = selected[0]
        removed_item = cart.pop(index)
        display_cart()
        messagebox.showinfo("Removed", f"{removed_item['name']} removed!")
    else:
        messagebox.showwarning("Error", "Select an item to remove!")

def update_item():
    selected = cart_listbox.curselection()
    if selected:
        index = selected[0]
        name = name_entry.get().strip()
        price = price_entry.get().strip()
        quantity = quantity_entry.get().strip()
        date = date_entry.get().strip()

        if not name or not price or not quantity or not date:
            messagebox.showwarning("Input Error", "Fill all fields!")
            return

        try:
            price = float(price)
            quantity = int(quantity)
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Input Error", "Enter valid price, quantity, and date (YYYY-MM-DD)!")
            return

        cart[index] = {"name": name, "price": price, "quantity": quantity, "date": date}
        display_cart()
        reset_fields()
    else:
        messagebox.showwarning("Error", "Select an item to update!")

def increase_quantity():
    selected = cart_listbox.curselection()
    if selected:
        index = selected[0]
        cart[index]["quantity"] += 1
        display_cart()

def decrease_quantity():
    selected = cart_listbox.curselection()
    if selected:
        index = selected[0]
        if cart[index]["quantity"] > 1:
            cart[index]["quantity"] -= 1
        else:
            messagebox.showwarning("Error", "Quantity cannot be less than 1!")
        display_cart()

def checkout():
    if not cart:
        messagebox.showinfo("Cart Empty", "Add items to cart before checkout!")
        return
    total = sum(item["price"] * item["quantity"] for item in cart)
    messagebox.showinfo("Checkout", f"Total Amount: ₹{total}\nThank you for shopping!")
    cart.clear()
    display_cart()

def display_cart():
    cart_listbox.delete(0, tk.END)
    for item in cart:
        cart_listbox.insert(tk.END, f"{item['name']} | ₹{item['price']} | Qty: {item['quantity']} | Date: {item['date']}")
    total = sum(item["price"] * item["quantity"] for item in cart)
    total_label.config(text=f"Total Price: ₹{total}")

def reset_fields():
    name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Advanced Shopping Cart")
root.geometry("700x600")
root.configure(bg="#f0f8ff")  # Light blue background

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=6)
style.configure("TLabel", font=("Helvetica", 12), background="#f0f8ff")
style.configure("TEntry", font=("Helvetica", 12))

# Title
ttk.Label(root, text="Advanced Shopping Cart", font=("Helvetica", 16, "bold")).pack(pady=10)

# Input Frame
frame = ttk.Frame(root)
frame.pack(pady=10)

ttk.Label(frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = ttk.Entry(frame, width=20)
name_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Price:").grid(row=0, column=2, padx=5, pady=5)
price_entry = ttk.Entry(frame, width=10)
price_entry.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(frame, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
quantity_entry = ttk.Entry(frame, width=10)
quantity_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame, text="Date (YYYY-MM-DD):").grid(row=1, column=2, padx=5, pady=5)
date_entry = ttk.Entry(frame, width=15)
date_entry.grid(row=1, column=3, padx=5, pady=5)

# Buttons Frame
btn_frame = ttk.Frame(root)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="Add Item", command=add_item).grid(row=0, column=0, padx=5)
ttk.Button(btn_frame, text="Update Item", command=update_item).grid(row=0, column=1, padx=5)
ttk.Button(btn_frame, text="Remove Item", command=remove_item).grid(row=0, column=2, padx=5)
ttk.Button(btn_frame, text="Increase Qty", command=increase_quantity).grid(row=0, column=3, padx=5)
ttk.Button(btn_frame, text="Decrease Qty", command=decrease_quantity).grid(row=0, column=4, padx=5)
ttk.Button(btn_frame, text="Checkout", command=checkout).grid(row=0, column=5, padx=5)
ttk.Button(btn_frame, text="Reset Fields", command=reset_fields).grid(row=0, column=6, padx=5)

# Cart Listbox
cart_listbox = tk.Listbox(root, width=90, height=20, font=("Helvetica", 12))
cart_listbox.pack(pady=10)

# Total Price
total_label = ttk.Label(root, text="Total Price: ₹0", font=("Helvetica", 14, "bold"))
total_label.pack(pady=10)

# Run GUI
root.mainloop()
