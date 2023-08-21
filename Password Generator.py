import tkinter as tk
import random
import string

def generate_password():
    password_length = length_var.get()

    if password_length <= 0:
        password_output.set("Invalid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_output.set(password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create a label and entry for password length
length_label = tk.Label(window, text="Password Length:")
length_label.pack()

length_var = tk.IntVar()
length_entry = tk.Entry(window, textvariable=length_var)
length_entry.pack()

# Create a button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Create a label to display the generated password
password_output = tk.StringVar()
password_label = tk.Label(window, textvariable=password_output)
password_label.pack()

# Start the GUI main loop
window.mainloop()
