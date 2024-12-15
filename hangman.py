import tkinter as tk
from tkinter import messagebox
import random

# List of words for the game
words = ["python", "hangman", "programming", "coding", "challenge","ram","shyam", "naresh"]

# Initialize variables
word_to_guess = random.choice(words)
guessed_letters = []
attempts = 6

# Create a window
window = tk.Tk()  # Corrected 'tk.tk()' to 'tk.Tk()'
window.title("Hangman Game")

# Function to check if the game is over
def is_game_over():
    return check_win() or check_loss()

# Function to check if the player has won
def check_win():
    return all(letter in guessed_letters for letter in word_to_guess)

# Function to check if the player has lost
def check_loss():
    return attempts == 0

# Function to handle a letter guess
def guess_letter():
    global attempts
    letter = letter_entry.get().lower()
    if letter.isalpha() and len(letter) == 1:
        if letter in guessed_letters:
            messagebox.showinfo("Hangman", f"You've already guessed '{letter}'")
        elif letter in word_to_guess:
            guessed_letters.append(letter)
            update_word_display()
            if check_win():
                messagebox.showinfo("Hangman", "Congratulations! You win!")
                reset_game()
        else:
            guessed_letters.append(letter)
            attempts -= 1
            update_attempts_display()
            draw_hangman()
            if check_loss():
                messagebox.showinfo("Hangman", "You lost! The word was: " + word_to_guess)
                reset_game()
    else:
        messagebox.showinfo("Hangman", "Please enter a single letter.")

# Function to reset the game
def reset_game():
    global word_to_guess, guessed_letters, attempts
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts = 6
    update_word_display()
    update_attempts_display()
    draw_hangman()

# Function to update the word display
def update_word_display():
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    word_label.config(text=display_word)

# Function to update the attempts display
def update_attempts_display():
    attempts_label.config(text=f"Attempts left: {attempts}")

# Function to draw the hangman figure
def draw_hangman():
    canvas.delete("hangman")
    if attempts < 6:
        canvas.create_oval(125, 125, 175, 175, width=4, tags="hangman")  # head
    if attempts < 5:
        canvas.create_line(150, 175, 150, 100, width=4, tags="hangman")  # body
    if attempts < 4:
        canvas.create_line(150, 150, 125, 125, width=4, tags="hangman")  # left arm
    if attempts < 3:
        canvas.create_line(150, 150, 175, 125, width=4, tags="hangman")  # right arm
    if attempts < 2:
        canvas.create_line(150, 200, 125, 250, width=4, tags="hangman")  # left leg
    if attempts < 1:
        canvas.create_line(150, 200, 175, 250, width=4, tags="hangman")  # right leg

# Create GUI elements
word_label = tk.Label(window, text="", font=("Arial", 24))
attempts_label = tk.Label(window, text="", font=("Arial", 16))  # Fixed label creation
letter_entry = tk.Entry(window, width=5, font=("Arial", 16))
guess_button = tk.Button(window, text="Guess", command=guess_letter)
reset_button = tk.Button(window, text="Reset", command=reset_game)
canvas = tk.Canvas(window, width=300, height=300)
canvas.create_line(50, 250, 250, 250, width=4)  # base line
canvas.create_line(200, 250, 200, 100, width=4)  # post
canvas.create_line(100, 100, 200, 100, width=4)  # beam

canvas.pack()

# Pack GUI elements
word_label.pack()
attempts_label.pack()
letter_entry.pack()
guess_button.pack()
reset_button.pack()

# Update initial display
update_word_display()
update_attempts_display()
draw_hangman()

# Run the application
window.mainloop()
