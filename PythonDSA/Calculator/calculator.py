import tkinter as tk

# ---------- DSA Logic ----------
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def apply_operation(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b

def evaluate_expression(expression):
    values = []
    ops = []
    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        if expression[i].isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = (val * 10) + int(expression[i])
                i += 1
            values.append(val)
        else:
            while ops and precedence(ops[-1]) >= precedence(expression[i]):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(apply_operation(val1, val2, op))
            ops.append(expression[i])
            i += 1
    while ops:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(apply_operation(val1, val2, op))
    return values[0]

# ---------- Tkinter GUI ----------
def press(key):
    entry_var.set(entry_var.get() + str(key))

def clear():
    entry_var.set("")

def calculate():
    try:
        expr = entry_var.get()
        result = evaluate_expression(expr)
        entry_var.set(str(result))
    except Exception as e:
        entry_var.set("Error")

# ---------- Window ----------
root = tk.Tk()
root.title("DSA Calculator")
root.geometry("300x400")
root.config(bg="#2c3e50")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=5, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

# ---------- Buttons ----------
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        action = lambda x=btn: press(x) if x not in ['C', '='] else calculate() if x=='=' else clear()
        b = tk.Button(frame, text=btn, font=("Arial", 18), command=action, bg="#34495e", fg="white", bd=1)
        b.pack(side="left", expand=True, fill="both")

root.mainloop()
