import tkinter as tk

def on_button_click(value):
    current_text = entry.get()
    new_text = current_text + value
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Syntax Error")

def clear():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create an entry widget for input and display
entry = tk.Entry(window, width=20, font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for digits and operators
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for label, row, col in buttons:
    button = tk.Button(window, text=label, width=5, height=2, font=("Helvetica", 16),
                       command=lambda label=label: on_button_click(label) if label != "=" else calculate())
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(window, text="C", width=5, height=2, font=("Helvetica", 16), command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Start the GUI main loop
window.mainloop()
