import random
import tkinter as tk
from tkinter import ttk, messagebox

# Stack class for storing guesses (DSA)
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

    def get_all(self):
        return self.items

# Game logic
class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game with Commit")
        self.master.geometry("450x450")
        self.master.configure(bg="#f0f8ff")

        self.guess_stack = Stack()
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.commit_file = "guess_history.txt"  # File to save committed guesses

        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=10)
        style.configure("TLabel", font=("Helvetica", 12))

        self.title_label = ttk.Label(self.master, text="Guess a number between 1 and 100", background="#f0f8ff")
        self.title_label.pack(pady=20)

        self.entry = ttk.Entry(self.master, font=("Helvetica", 14))
        self.entry.pack(pady=10)

        self.guess_button = ttk.Button(self.master, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.commit_button = ttk.Button(self.master, text="Commit Guesses", command=self.commit_guesses)
        self.commit_button.pack(pady=10)

        self.result_label = ttk.Label(self.master, text="", background="#f0f8ff")
        self.result_label.pack(pady=10)

        self.guess_list_label = ttk.Label(self.master, text="Your guesses: []", background="#f0f8ff")
        self.guess_list_label.pack(pady=10)

        self.reset_button = ttk.Button(self.master, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def make_guess(self):
        try:
            guess = int(self.entry.get())
            self.entry.delete(0, tk.END)
            self.guess_stack.push(guess)
            self.attempts += 1

            if guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.", foreground="blue")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.", foreground="red")
            else:
                self.result_label.config(text=f"Congratulations! You guessed it in {self.attempts} attempts.", foreground="green")
                messagebox.showinfo("Winner", f"You guessed the number {self.number_to_guess} correctly!")

            self.guess_list_label.config(text=f"Your guesses: {self.guess_stack.get_all()}")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

    # Commit feature: save guesses to a file
    def commit_guesses(self):
        guesses = self.guess_stack.get_all()
        if not guesses:
            messagebox.showwarning("No guesses", "No guesses to commit!")
            return
        with open(self.commit_file, "a") as file:
            file.write(",".join(map(str, guesses)) + "\n")
        messagebox.showinfo("Committed", f"Guesses committed to {self.commit_file}")
        self.guess_stack = Stack()  # Clear stack after commit
        self.guess_list_label.config(text="Your guesses: []")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.guess_stack = Stack()
        self.attempts = 0
        self.result_label.config(text="")
        self.guess_list_label.config(text="Your guesses: []")
        self.entry.delete(0, tk.END)

# Run the game
root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()
