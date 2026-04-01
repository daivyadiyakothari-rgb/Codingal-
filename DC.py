# Denomination calculator
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from Tk2 import topwin

# Setting up Main Window
root = Tk()
root.title("Denomination Calculator")
root.configure(bg="#f0f0f0")
root.geometry("400x300")

# Adding Image and Labels in the Main Window
upload = Image.open ("Bhavya.jpg")

# Resizing the image
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg="#f0f0f0")
label.place(x=50, y=20)
label1 = Label(root, text="Enter the amount:", font=("Arial", 12), bg="#f0f0f0")
label1.place(x=50, y=250)

Label1 = Label(root, 
               text="Hey User! Welcome to Denomination Counter Application.",
               bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function to calculate the denominations
def msg():
    MsgBox = messagebox.showinfo(
    "Alert", "Do you want to calculate the denomination count?")
    if MsgBox =='ok':
        topwin()
# Adding Entry and Button in the Main Window
button1 = Button(root,
    text="Let's get started!",
    command=msg,
    bg="light blue",
    fg='white')
button1.place(relx=0.5, y=280, anchor=CENTER)

def topwin():
    # Top Window
    top = Toplevel(root)
    top.title("Denomination Calculator")
    top.geometry("400x300")
    top.configure(bg="#f0f0f0")

# Centering the Top Window
label.place(x=230, y=50)
entry.place(x=200, y =80)
btn.place(x=240, y=120)
lbl.place(x=140, y=170)

l1.place(x=180, y=200)
l2.place(x=180, y=230)
l3.place(x=180, y=260)

top.mainloop()

root.mainloop()
