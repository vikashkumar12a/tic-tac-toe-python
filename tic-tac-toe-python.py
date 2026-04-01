import tkinter as tk
from tkinter import messagebox

# Function to check for a winne

def check_winner():
    # List of all winning combinations (rows, columns, diagonals)
    global winner
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
         # Check if all three buttons in combo have the same text and not empty
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            # Highlight winning buttons
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            # Show a messagebox with the winner
            winner = True  
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            return

# Function when a button is clicked

def button_click(index):
     # Only allow click if button is empty and winner is False
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player # Mark the button with X or O
        check_winner()  
        if not winner:
            toggle_player()

# Function to switch between X and O
def toggle_player():
    global current_player
    # Toggle the current player
    current_player = "X" if current_player == "O" else "O"
     # Update the label to show whose turn
    label.config(text=f"Player {current_player}'s turn")


# GUI Setup
root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

# Place buttons in a 3x3 grid
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = "X" # Starting player
winner = False  # Flag to track if someone has won

# Label to display current player's turn
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Start the GUI event loop
root.mainloop()