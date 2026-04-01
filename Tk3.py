# After Class Project
import tkinter as tk
import random

# choices
choices = ["Rock", "Paper", "Scissors"]

# function to play game
def play(user_choice):
    computer_choice = random.choice(choices)

    # show computer choice
    computer_label.config(text="Computer chose: " + computer_choice)

    # check winner
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "You Lose!"

    result_label.config(text=result)

# create window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

# title label
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16))
title_label.pack(pady=10)

# buttons
rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.pack(pady=5)

# computer choice label
computer_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12))
computer_label.pack(pady=10)

# result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# run window
root.mainloop()
