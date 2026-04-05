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

# After Class Project
from tkinter import *
import random

# create window
root = Tk()
root.title("Tic Tac Toe")

# variables
current_player = "X"
buttons = []
game_active = True

# check winner
def check_winner():
    global game_active

    # rows
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            game_active = False
            return buttons[row][0]["text"]

    # columns
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            game_active = False
            return buttons[0][col]["text"]

    # diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        game_active = False
        return buttons[0][0]["text"]

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        game_active = False
        return buttons[0][2]["text"]

    # draw
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return None

    game_active = False
    return "Draw"

# button click
def button_click(row, col):
    global current_player

    if buttons[row][col]["text"] == "" and game_active:
        buttons[row][col]["text"] = current_player

        winner = check_winner()

        if winner:
            if winner == "Draw":
                status_label.config(text="It's a Draw!")
            else:
                status_label.config(text=winner + " Wins!")
        else:
            # switch player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

            status_label.config(text="Turn: " + current_player)

# restart game
def restart_game():
    global current_player, game_active

    current_player = "X"
    game_active = True
    status_label.config(text="Turn: X")

    for row in buttons:
        for btn in row:
            btn["text"] = ""

# create buttons
for i in range(3):
    row = []
    for j in range(3):
        btn = Button(root, text="", font=("Arial", 20), width=5, height=2,
                     command=lambda r=i, c=j: button_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

# status label
status_label = Label(root, text="Turn: X", font=("Arial", 14))
status_label.grid(row=3, column=0, columnspan=3)

# restart button
restart_btn = Button(root, text="Restart", command=restart_game)
restart_btn.grid(row=4, column=0, columnspan=3)

# run app
root.mainloop()
