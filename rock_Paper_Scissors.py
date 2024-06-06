from tkinter import *
from random import randint
from PIL import ImageTk, Image

# Initialize the main window
w = Tk()
w.title("Rock Paper Scissors")
w.config(bg="black")
w.geometry("600x500")

# Function to resize images
def resize_image(image_path, size):
    img = Image.open(image_path)
    img = img.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)

# Load and resize images
rock = resize_image("rock.png", (400, 300))
paper = resize_image("paper.png", (400, 300))
scissors = resize_image("scissors.png", (400, 300))
rock_opp = resize_image("rock_opp.png", (400, 300))
paper_opp = resize_image("paper_opp.png", (400, 300))
scissors_opp = resize_image("scissors_opp.png", (400, 300))

# Labels for user and opponent images
user = Label(w, image=rock, bg='black')
opp = Label(w, image=rock_opp, bg='black')
user.grid(row=1, column=0, padx=20, pady=20)
opp.grid(row=1, column=4, padx=20, pady=20)

# Score labels
user_score = Label(w, text=0, font=("Arial", 24, "bold"), bg='black', fg='white')
opp_score = Label(w, text=0, font=("Arial", 24, "bold"), bg='black', fg='white')
user_score.grid(row=1, column=1, padx=10)
opp_score.grid(row=1, column=3, padx=10)

# Indicators
user_indicate = Label(w, font=("Arial", 16, "bold"), text='User', bg='black', fg='lightgreen')
user_indicate.grid(row=0, column=1, pady=10)
opp_indicate = Label(w, font=("Arial", 16, "bold"), text='Opponent', bg='black', fg='red')
opp_indicate.grid(row=0, column=3, pady=10)

# Message label
message = Label(w, font=("Arial", 20, "bold"), bg='black', fg='white', text='')
message.grid(row=6, column=2, pady=20)

def update_message(x):
    message.config(text=x)

def upd_userScore():
    score = int(user_score["text"])
    score += 1
    user_score["text"] = str(score)

def upd_oppScore():
    score = int(opp_score["text"])
    score += 1
    opp_score["text"] = str(score)

def winner(user, opponent):
    if user == opponent:
        update_message("Tie!!")
    elif user == "rock":
        if opponent == "paper":
            update_message("You lose")
            upd_oppScore()
        else:
            update_message("You win")
            upd_userScore()
    elif user == "paper":
        if opponent == "scissors":
            update_message("You lose")
            upd_oppScore()
        else:
            update_message("You win")
            upd_userScore()
    elif user == "scissors":
        if opponent == "rock":
            update_message("You lose")
            upd_oppScore()
        else:
            update_message("You win")
            upd_userScore()

valid_choice = ["rock", "paper", "scissors"]

def choice(x):
    # Opponent choice
    opp_choice = valid_choice[randint(0, 2)]
    if opp_choice == "rock":
        opp.config(image=rock_opp)
    elif opp_choice == "paper":
        opp.config(image=paper_opp)
    else:
        opp.config(image=scissors_opp)

    # User choice
    if x == "rock":
        user.config(image=rock)
    elif x == "paper":
        user.config(image=paper)
    else:
        user.config(image=scissors)

    winner(x, opp_choice)

# Buttons for user choices
rock_button = Button(w, command=lambda: choice("rock"), width=12, height=3, text='Rock', bg='deep pink', fg='black', font=("Arial", 14, "bold"))
rock_button.grid(row=2, column=1, pady=10)
paper_button = Button(w, command=lambda: choice("paper"), width=12, height=3, text='Paper', bg='yellow', fg='black', font=("Arial", 14, "bold"))
paper_button.grid(row=2, column=2, pady=10)
scissors_button = Button(w, command=lambda: choice("scissors"), width=12, height=3, text='Scissors', bg='royal blue', fg='black', font=("Arial", 14, "bold"))
scissors_button.grid(row=2, column=3, pady=10)

# Adding decorative elements
separator = Frame(w, height=2, bd=1, relief=SUNKEN, bg='white')
separator.grid(row=3, column=0, columnspan=5, pady=10, sticky="we")

# Finalize the main loop
w.mainloop()
