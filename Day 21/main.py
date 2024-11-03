'''
🐍 (Py100: 100 Days of Python Challenge)
Author: Saif Khan
-----------------------------------
Day 21 - Snake Game Part 2
-----------------------------------
This project is an extension of the classic Snake Game. The snake can now eat food to grow and
earn points, and the game keeps track of the score. The game ends if the snake collides with
the wall or its own tail. The screen and game logic have been enhanced to provide a better
gaming experience.
-----------------------------------
'''

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)  # Set the window size
screen.bgcolor("black")  # Set the background color to black
screen.title("My Snake Game")  # Set the window title
screen.tracer(0)  # Turn off the animation to manually update the screen

# Initialize game objects
snake = Snake()  # Create the snake
food = Food()  # Create the food
scoreboard = Scoreboard()  # Create the scoreboard

# Set up the keyboard listeners for snake control
screen.listen()  # Start listening for key presses
screen.onkey(snake.up, "Up")  # Move up when "Up" key is pressed
screen.onkey(snake.down, "Down")  # Move down when "Down" key is pressed
screen.onkey(snake.left, "Left")  # Move left when "Left" key is pressed
screen.onkey(snake.right, "Right")  # Move right when "Right" key is pressed

# Start the game loop
game_is_on = True
while game_is_on:
    screen.update()  # Update the screen with the latest frame
    time.sleep(0.1)  # Pause the game for a moment to slow down the snake
    snake.move()  # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:  # Check if the snake's head is close to the food
        food.refresh()  # Move the food to a new random position
        snake.extend()  # Add a segment to the snake
        scoreboard.increase_score()  # Update the score

    # Detect collision with wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor() < -280):
        game_is_on = False  # End the game
        scoreboard.game_over()  # Display "Game Over" message

    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            continue  # Skip checking collision with the head itself
        if snake.head.distance(segment) < 10:  # Check if the head touches any segment
            game_is_on = False  # End the game
            scoreboard.game_over()  # Display "Game Over" message

# Close the game window when clicked
screen.exitonclick()
