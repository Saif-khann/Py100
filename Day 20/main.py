'''
🐍(Py100: 100 Days of Python Challenge)
Author: Saif Khan
-----------------------------------
Day 20 Project: Snake Game - Part 1
-----------------------------------
Description: This project creates a classic Snake Game using the Turtle graphics library in Python.
The snake moves in a 600x600 window, and the player can control its direction using arrow keys.
In this version, the game setup and basic snake movement are implemented.
'''

from turtle import Screen
from snake import Snake
import time

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)  # Set screen dimensions
screen.bgcolor("black")  # Set background color to black
screen.title("My Snake Game")  # Set the window title
screen.tracer(0)  # Turn off automatic animation updates

# Create a Snake object
snake = Snake()

# Set up key listeners to control the snake's movement
screen.listen()
screen.onkey(snake.up, "Up")  # Move up when the "Up" arrow key is pressed
screen.onkey(snake.down, "Down")  # Move down when the "Down" arrow key is pressed
screen.onkey(snake.left, "Left")  # Move left when the "Left" arrow key is pressed
screen.onkey(snake.right, "Right")  # Move right when the "Right" arrow key is pressed

# Start the game loop
game_is_on = True
while game_is_on:
    screen.update()  # Refresh the screen to display changes
    time.sleep(0.1)  # Pause the game for a short moment

    # Move the snake forward
    snake.move()

# Close the screen when clicked
screen.exitonclick()
