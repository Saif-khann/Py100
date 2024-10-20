'''
🐍 (Py100: 100 Days of Python Challenge)
Author: Saif Khan
-----------------------------------
Day 7: Hangman Project
-----------------------------------
This project is a game of Hangman where a random word is chosen, and the player has to guess the letters in the word. 
The player starts with 6 lives.
Each incorrect guess reduces the player's lives, and the game ends when the player either guesses all the letters (win) or loses all lives (lose).
The program uses predefined hangman art and word lists from external files `hangman_art.py` and `hangman_words.py`.
'''
import random

# Importing word list and hangman art (stages and logo) from external files
from hangman_words import word_list
from hangman_art import stages, logo

# The player starts with 6 lives
lives = 6

# Print the hangman logo at the start of the game
print(logo)

# Randomly select a word from the word list
chosen_word = random.choice(word_list)
# print(chosen_word)  # For testing purposes, this prints the chosen word (should be removed in real gameplay)

# Create a placeholder for the word to guess with underscores (_)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# Game status variables
game_over = False  # To track if the game has ended
correct_letters = []  # List to store correctly guessed letters

# Main game loop: continues until the player wins or loses
while not game_over:

    # Display the current number of lives remaining
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    
    # Prompt the player to guess a letter, and ensure the guess is in lowercase
    guess = input("Guess a letter: ").lower()

    # If the player has already guessed the letter, notify them
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""  # Variable to build the current state of the word being guessed

    # Loop through each letter in the chosen word
    for letter in chosen_word:
        # If the guessed letter is in the word, reveal it in the display
        if letter == guess:
            display += letter
            correct_letters.append(guess)  # Add the correct guess to the correct_letters list
        # If the letter has already been correctly guessed before, keep it in the display
        elif letter in correct_letters:
            display += letter
        # If the letter hasn't been guessed, show an underscore
        else:
            display += "_"

    # Show the current state of the word being guessed
    print("Word to guess: " + display)

    # If the guessed letter is not in the word, reduce lives
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        # If the player runs out of lives, end the game and reveal the word
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    # If there are no more underscores, the player has guessed the word and wins
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Display the current stage of the hangman art, based on the remaining lives
    print(stages[lives])
