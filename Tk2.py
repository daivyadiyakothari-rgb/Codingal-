import tkinter as tk
import random
import string

# Function to generate password
def generate_password():
    length = int(length_entry.get())

    # Combine all character types
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for i in range(length))

    # Display password
    result_var.set(password)

# Create window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x250")

# Title Label
title_label = tk.Label(root, text="Password Generator", font=("Arial", 16))
title_label.pack(pady=10)

# Length input
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

# Button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

# Result display
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

# Run app
root.mainloop() 
