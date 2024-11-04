'''
🏓 (Py100: 100 Days of Python Challenge)
Author: Saif Khan
-----------------------------------
Day 22 Project: Classic Pong Game Using Turtle Graphics
-----------------------------------
Description:
This project is a recreation of the classic Pong game, built using Python's Turtle graphics module.
The game consists of two paddles, a bouncing ball, and a scoring system. Players can control the 
paddles to keep the ball from passing their side, and each missed ball results in a point for the 
opposing player. The game continues indefinitely, updating and moving at a dynamic speed.
'''

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the main game screen
screen = Screen()
screen.bgcolor("black")  # Set the background color to black
screen.setup(width=800, height=600)  # Set screen dimensions
screen.title("Pong")  # Set the window title
screen.tracer(0)  # Turn off animation for smoother updates

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))  # Right paddle at position (350, 0)
l_paddle = Paddle((-350, 0))  # Left paddle at position (-350, 0)
ball = Ball()  # The ball object that will move and bounce
scoreboard = Scoreboard()  # Scoreboard to keep track of points

# Set up key listeners for paddle movement
screen.listen()
screen.onkey(r_paddle.go_up, "Up")  # Move right paddle up with the "Up" arrow key
screen.onkey(r_paddle.go_down, "Down")  # Move right paddle down with the "Down" arrow key
screen.onkey(l_paddle.go_up, "w")  # Move left paddle up with the "w" key
screen.onkey(l_paddle.go_down, "s")  # Move left paddle down with the "s" key

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Control ball speed
    screen.update()  # Update screen animations
    ball.move()  # Move the ball

    # Detect collision with top or bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # Reverse ball's y-direction

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()  # Reverse ball's x-direction and speed up

    # Detect if the right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()  # Reset ball to the center
        scoreboard.l_point()  # Increase left paddle's score

    # Detect if the left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()  # Reset ball to the center
        scoreboard.r_point()  # Increase right paddle's score

screen.exitonclick()  # Close the screen on click
