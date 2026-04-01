# Activity 1: 
from struct import pack
from tkinter import *
from PIL import Image, ImageTk
# Create a window with a title bar and set its geometry as well
root = Tk()
root.title('image')
root.geometry('400x400')

# Now use Image.open to open and identify the given image file.
upload = Image.open("img.jpg")

# Convert this Image to Tkinter compatible image
image = ImageTk. PhotoImage(upload)

# Add image to Tkinter Label
label = Label(root, image=image, height=350, width=300)
label.place( x = 50 , y = 0 )
label2 = Label(root, text="This is how you add image in Tkinter Window")
label2.place( x = 40 , y = 360 )

# Run the application
root.mainloop()

# Activity 2
# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
root = Tk()
root.geometry("200x200")

# Function for Displaying Warning Message
# This will be called once the button is clicked
# messagebox.showwarning("Window Name", "Text to be displayed")
def msg():
  messagebox.showwarning("Alert", "Stop! Virus Found.")

# Adding Button Widget to Window
button = Button(root, text="Scan for Virus", command=msg)
button.place( x = 40 , y = 80 )

# Entering main event loop
root.mainloop()

# Activity 3

# Import necessary libraries from tkinter import *
# Setting up Main Window
root = Tk()
root.geometry("400x300")
root.title("main")

# Function to open New (Top Level) Window
def topwin():
    # Setting up Top Window
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")

    # Adding a label widget to Top Window
    l2 = Label(top, text = "This is toplevel window")
    l2.pack()
    top.mainloop()

# Adding a label and button Widget to Root (Main) Window
l = Label(root, text = "This is root window")
btn = Button(root, text = "Click here to open another window",
command = topwin)

# Arranging widgets
l.pack()
btn.pack()

# After Class Project
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
