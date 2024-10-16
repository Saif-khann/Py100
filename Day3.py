# 🐍 (Py100: 100 Days of Python Challenge)
# Author: Saif Khan
# ----------------------------------------------
# Day 3 Project: Treasure Island 🏝️
# ----------------------------------------------
# Create a fun text-based adventure game where the user navigates through obstacles to find a hidden treasure.

# Description:
# 1. Greet the user and introduce the adventure game.
# 2. Use ASCII art to display a title for the game.
# 3. Present the user with multiple choices as they navigate through a series of obstacles (e.g., crossing roads, lakes, and choosing doors).
# 4. Depending on their decisions, they either win the game by finding the treasure or face different outcomes (game over scenarios).
# 5. Ensure the input choices are case-insensitive for better user experience.

# Code starts here...

print(r'''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|''') 
# Used raw string (r''') to prevent escape warnings for the ASCII art

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") # Introduction to the game and mission

# First choice: user is asked to choose a direction at the crossroad
first_obstacle = input('You\'re at a cross road. Where do you want to go? Type "left" or "right": \n').lower() 
# Added .lower() to make the input case-insensitive for easier user interaction (basically any input the user gives it gets converted to lower characters)

if first_obstacle == "left":  # Player chose to go left
    # Second choice: the player arrives at a lake and must choose whether to wait for a boat or swim across
    second_obstacle = input('''You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across: \n''').lower()
    
    if second_obstacle == "wait":  # Player chose to wait for a boat
        # Third choice: player reaches the island and must choose a door color
        third_obstacle = input('''You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose: \n''').lower()
        
        if third_obstacle == "yellow":  # Winning choice
            print("You found the treasure! You Win!") # Player wins the game
        elif third_obstacle == "red":  # Game over scenario 1
            print("It's a room full of fire. Game Over.") # Losing scenario - fire room
        else:  # Game over scenario 2
            print("You enter a room of beasts. Game Over!") # Losing scenario - beasts room
    else:
        print("You get attacked by an angry trout. Game Over!") # Losing scenario - attacked by a trout

else:
    print("You fell into a hole. Game Over!") # Losing scenario - falling into a hole


