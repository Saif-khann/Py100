'''
🃏 (Py100: 100 Days of Python Challenge)
Author: Saif Khan
-----------------------------------
Day 11: Blackjack Game Simulation
-----------------------------------
This program simulates a simple game of Blackjack, where the
user and the computer are dealt cards, and the objective is
to get as close to 21 points as possible without going over.
It incorporates game logic like dealing cards, calculating
scores, handling Blackjacks, and comparing the results.
-----------------------------------
'''

import random
from art import logo  # Importing logo for visual display at the start of the game

# Function to randomly deal a card from the deck
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # The deck of cards, where 11 represents Ace
    card = random.choice(cards)  # Randomly choosing one card
    return card  # Returning the chosen card

# Function to calculate the total score of the cards in hand
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    
    # If there's a Blackjack (21 with two cards: an Ace and a 10), return 0 to represent it
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # If the hand contains an Ace (11) and the total score exceeds 21, convert Ace to 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)  # Return the total sum of the cards

# Function to compare user and computer scores and determine the winner
def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"  # Both scores are the same
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"  # Computer has Blackjack (0 means Blackjack)
    elif u_score == 0:
        return "Win with a Blackjack 😎"  # User has Blackjack
    elif u_score > 21:
        return "You went over. You lose 😭"  # User score exceeds 21, user loses
    elif c_score > 21:
        return "Opponent went over. You win 😁"  # Computer score exceeds 21, user wins
    elif u_score > c_score:
        return "You win 😃"  # User has a higher score than the computer
    else:
        return "You lose 😤"  # Computer has a higher score than the user

# Function to play a game of Blackjack
def play_game():
    print(logo)  # Displaying the game logo

    # Initializing hands and game status
    user_cards = []
    computer_cards = []
    is_game_over = False  # Control variable to track if the game is over

    # Dealing two cards to both the user and the computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Looping while the game is still active
    while not is_game_over:
        # Calculate scores for both user and computer
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Display the user's current cards and score, and the computer's first card
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check if the game should end (Blackjack or user score exceeds 21)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask the user if they want another card or not
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())  # Deal another card to the user
            else:
                is_game_over = True  # User decided to pass, end the loop

    # Computer keeps drawing cards until its score reaches 17 or higher
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Display the final scores and hands, then compare them to declare the winner
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))  # Compare user and computer scores and display the result

# Game loop: Ask the user if they want to play a game of Blackjack
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)  # Clear the screen by printing new lines
    play_game()  # Start the Blackjack game
