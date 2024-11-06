'''
🌎 (Py100: 100 Days of Python Challenge)
Author: Saif Khan
-----------------------------------
Day 25 Project: U.S. States Game
-----------------------------------
Description:
This script creates an interactive game using the Turtle graphics library and the Pandas library
to help users learn the names of all 50 U.S. states. When the game starts, an empty U.S. map is displayed,
and the user is prompted to input state names one by one. Correct guesses are displayed on the map.
The game continues until all 50 states are guessed or the user exits. The states not guessed are saved
to a CSV file for further learning.

Note: Make sure to have the 'pandas' library installed to run this script.
You can install it using: pip install pandas
-----------------------------------
'''

import turtle
import pandas

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load the image of the blank U.S. map
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load the data from the CSV file
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Main game loop
while len(guessed_states) < 50:
    # Prompt user to enter a state's name, showing the number of states guessed correctly
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    ).title()

    # Check if the user wants to exit the game
    if answer_state == "Exit":
        # Create a list of states that were not guessed
        missing_states = [state for state in all_states if state not in guessed_states]
        
        # Save the missing states to a new CSV file
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # If the answer is correct, display the state name on the map
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()  # Hide the turtle cursor
        t.penup()  # Lift the pen to avoid drawing lines
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())  # Move to the state's coordinates
        t.write(answer_state)  # Write the state name
