import tkinter as tk
from tkinter import ttk
import random

## GUI PART

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create a label to display the result
result_label = ttk.Label(root, text="Choose Rock, Paper, or Scissors")
result_label.pack()

# Create buttons for Rock, Paper, and Scissors
rock_button = ttk.Button(root, text="Rock")
paper_button = ttk.Button(root, text="Paper")
scissors_button = ttk.Button(root, text="Scissors")

rock_button.pack()
paper_button.pack()
scissors_button.pack()

## GAME LOGIC

# Function to determine the winner
def determine_winner(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        return f"You chose {player_choice}, computer chose {computer_choice}. You win!"
    else:
        return f"You chose {player_choice}, computer chose {computer_choice}. Computer wins!"

# Function to handle button clicks
def on_button_click(choice):
    result = determine_winner(choice)
    result_label.config(text=result)

# Bind the buttons to their respective functions
rock_button.config(command=lambda: on_button_click("Rock"))
paper_button.config(command=lambda: on_button_click("Paper"))
scissors_button.config(command=lambda: on_button_click("Scissors"))

# Start the GUI main loop
root.mainloop()

