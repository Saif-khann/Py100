# scoreboard.py - Scoreboard Class
# This file contains the Scoreboard class, which is responsible for displaying and updating
# the score of the snake game. It also displays a "Game Over" message when the game ends.

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0  # Initialize the score
        self.color("white")  # Set the text color to white
        self.penup()  # Lift the pen to avoid drawing
        self.goto(0, 270)  # Position the scoreboard at the top of the screen
        self.hideturtle()  # Hide the turtle icon
        self.update_scoreboard()  # Display the initial score

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  # Display the score

    def game_over(self):
        self.goto(0, 0)  # Move to the center of the screen
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)  # Display "Game Over" message

    def increase_score(self):
        self.score += 1  # Increase the score by 1
        self.clear()  # Clear the previous score
        self.update_scoreboard()  # Update the score display
