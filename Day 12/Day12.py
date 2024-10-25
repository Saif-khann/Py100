# 🎲 (Py100: 100 Days of Python Challenge)
# Author: Saif Khan

# -------------------------------------------------------------
# Day 12: Number Guessing Game
# This program is a number guessing game where the player tries 
# to guess a randomly chosen number between 1 and 100. The player 
# selects a difficulty level, which determines the number of guesses 
# allowed. After each guess, the program gives hints and tracks 
# the remaining attempts until the player wins or runs out of attempts.
# -------------------------------------------------------------

from random import randint
from art import logo

# Constants for the number of turns based on difficulty level
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check the user's guess against the actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess and returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1  # Decrease turn count if guess is too high
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1  # Decrease turn count if guess is too low
    else:
        print(f"You got it! The answer was {actual_answer}")  # Correct guess

# Function to set the difficulty level based on user's choice
def set_difficulty():
    """Sets the difficulty level and returns the number of turns."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS  # Easy level with more turns
    else:
        return HARD_LEVEL_TURNS  # Hard level with fewer turns

# Main function to run the guessing game
def game():
    print(logo)  # Display the game logo
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random answer and print a hint (optional)
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    # Get the number of turns based on chosen difficulty
    turns = set_difficulty()

    guess = 0  # Initialize guess variable to start the game loop
    # Continue until the guess is correct or turns run out
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        
        # Prompt user to make a guess and update the turns based on result
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        # End game if no turns are left
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")  # Prompt to guess again if incorrect

# Start the game
game()
