'''
🐍 (Py100: 100 Days of Python Challenge)
Author: Saif Khan
----------------------------------------------
Day 4 Project: Rock Paper Scissors Game ✊🖐️✌️
----------------------------------------------
Create a simple game where the user plays Rock, Paper, Scissors against the computer.

Description:
1. The user will choose between Rock, Paper, and Scissors by typing 0, 1, or 2.
2. The program will randomly select Rock, Paper, or Scissors for the computer.
3. The choices will be visually displayed using ASCII art.
4. The winner is determined by the rules of Rock, Paper, Scissors.
5. If the user enters an invalid choice, an error message will be displayed.

Code starts here...
'''

import random  # Importing random to let the computer make random choices

# ASCII art for Rock, Paper, Scissors
rock = r'''
  .----.-----.-----.-----.
 /      \     \     \     \
|  \/    |     |   __L_____L__
|   |    |     |  (           \
|    \___/    /    \______/    |
|        \___/\___/\___/       |
 \      \     /               /
  |                        __/
   \_                   __/
    |        |         |
    |                  |
    |                  |'''

paper = r''' 
         /"\
     /"\|\./|/"\
    |\./|   |\./|
    |   |   |   |
    |   |>~<|   |/"\
    |>~<|   |>~<|\./|
    |   |   |   |   |
/~T\|   |   =[@]=   |
|_/ |   |   |   |   |
|   | ~   ~   ~ |   |
|~< |             ~ |
|   '               |
\                   |
 \                 /
  \               /
   \.            /
     |          |
     |          |'''

scissors = r'''
              ____
  ____       /    \
 |    \      |    |
 \     \     | . .|
  \ . ' \    |    |
   \     \   | . .|
    \ . ' \  |    |
   __\     \_| . .|
  /   \ . '       |
  \   _\_______   |
 __\ (         \  |
/   \ \_____.   \ |
\   \`---'  \    \|
 \   \      /     |
  `---'    /      |
    \      |      /
     \___________/'''

# Store the ASCII art in a list to easily display them based on user input
images = [rock, paper, scissors]

# Prompt the user to choose Rock, Paper, or Scissors using numbers
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
print(f"You chose:\n {images[userChoice]}\n")  # Display the user's choice using ASCII art

# Randomly choose for the computer (0 for Rock, 1 for Paper, 2 for Scissors)
computerChoice = random.randint(0, 2)
print(f"Computer chose:\n {images[computerChoice]}\n")  # Display the computer's choice using ASCII art

# Check if the user input is valid
if userChoice >= 3 or userChoice < 0:
    print("Invalid choice!")  # Handle invalid input by the user
# Determine the winner based on game rules
elif userChoice == 0 and computerChoice == 2:
    print("You Win!")  # Rock beats Scissors
elif computerChoice == 0 and userChoice == 2:
    print("You Lose!")  # Scissors lose to Rock
elif computerChoice > userChoice:
    print("You Lose!")  # If the computer's choice beats the user's choice
elif userChoice > computerChoice:
    print("You Win!")  # If the user's choice beats the computer's choice
elif userChoice == computerChoice:
    print("It's a Draw!")  # If both choices are the same, it's a draw



