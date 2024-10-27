'''
🎲 (Py100: 100 Days of Python Challenge)
Author: Saif Khan
-----------------------------------
Day 14: Higher Lower Game
-----------------------------------
This program is a 'Higher Lower' game where the player tries 
to guess which of two Instagram accounts has more followers.
The player continues guessing and earning points until they 
make a wrong guess. The game utilizes random account data 
and provides continuous feedback and score tracking.
-----------------------------------
'''

# Import necessary modules and data
from art import logo, vs
from game_data import data
import random

# Function to format the account data for display
def format_data(account):
    """Takes the account data and returns it in a printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

# Function to check if the user's guess is correct
def check_answer(guess, a_followers, b_followers):
    """Takes a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Display the game logo
print(logo)
score = 0
game_should_continue = True

# Generate a random account from the game data to start the game
account_b = random.choice(data)

# Main game loop to make the game repeatable
while game_should_continue:
    # Set account_a to the previous account_b and generate a new account_b
    account_a = account_b
    account_b = random.choice(data)

    # Ensure account_b is not the same as account_a
    while account_a == account_b:
        account_b = random.choice(data)

    # Display the comparison data to the user
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask the user for their guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen and redisplay the game logo
    print("\n" * 20)
    print(logo)

    # Get the follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check if the user's guess is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give feedback to the user and update the score if correct
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False  # End the game if the guess is wrong
