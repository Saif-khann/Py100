'''
🐢 (Py100: 100 Days of Python Challenge)
Author: Saif Khan
-----------------------------------
Day 19 Project: Turtle Racing Game
-----------------------------------
Description: 
A fun turtle racing game where the player bets on which turtle will win.
The turtles move a random distance in each loop iteration until one crosses the finish line.
-----------------------------------
'''

from turtle import Turtle, Screen
import random

# Set up the race flag as inactive initially
is_race_on = False

# Set up the screen size and prompt the user for their bet
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Define colors and starting y-positions for the turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create 6 turtle racers and set their starting positions
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()  # Lift the pen so the turtle doesn't draw lines
    new_turtle.color(colors[turtle_index])  # Set the turtle's color
    new_turtle.goto(x=-230, y=y_positions[turtle_index])  # Place turtle at starting position
    all_turtles.append(new_turtle)  # Add each turtle to the list of racers

# Start the race if the user has placed a bet
if user_bet:
    is_race_on = True

# While the race is active, move each turtle forward by a random distance
while is_race_on:
    for turtle in all_turtles:
        # Check if a turtle has crossed the finish line (230 is 250 - half the turtle width)
        if turtle.xcor() > 230:
            is_race_on = False  # End the race
            winning_color = turtle.pencolor()  # Get the color of the winning turtle
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")  # User wins
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")  # User loses

        # Move the turtle forward by a random distance (0 to 10 units)
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Close the screen when clicked
screen.exitonclick()
