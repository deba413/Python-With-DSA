import tkinter as tk
from tkinter import messagebox

# ---------- DSA Logic ----------
tasks = []  # List to store tasks

def add_task():
    task = task_entry.get()
    if task.strip() == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return
    tasks.append(task)  # DSA: Adding to list
    task_entry.delete(0, tk.END)
    update_task_list()

def delete_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task to delete!")
        return
    index = selected[0]
    tasks.pop(index)  # DSA: Remove from list
    update_task_list()

def update_task_list():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        task_listbox.insert(tk.END, f"{idx + 1}. {task}")

# ---------- GUI ----------
root = tk.Tk()
root.title("DSA To-Do List / Task Manager")
root.geometry("400x500")
root.config(bg="#2c3e50")

# Heading
heading = tk.Label(root, text="To-Do List", bg="#2c3e50", fg="white", font=("Arial", 24, "bold"))
heading.pack(pady=10)

# Task entry
task_entry = tk.Entry(root, font=("Arial", 16), bd=4, relief="ridge")
task_entry.pack(pady=10, padx=10, fill="x")

# Buttons frame
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=5)

add_btn = tk.Button(button_frame, text="Add Task", command=add_task, bg="#27ae60", fg="white", font=("Arial", 14), width=10)
add_btn.grid(row=0, column=0, padx=5, pady=5)

delete_btn = tk.Button(button_frame, text="Delete Task", command=delete_task, bg="#c0392b", fg="white", font=("Arial", 14), width=10)
delete_btn.grid(row=0, column=1, padx=5, pady=5)

# Task listbox
task_listbox = tk.Listbox(root, font=("Arial", 16), bd=3, relief="ridge", selectbackground="#2980b9", activestyle="none")
task_listbox.pack(pady=10, padx=10, fill="both", expand=True)

root.mainloop()
 