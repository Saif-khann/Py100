from turtle import Turtle

# Constants for font style
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1  # Initialize level
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)  # Position scoreboard at the top left
        self.update_scoreboard()

    def update_scoreboard(self):
        # Update and display the current level
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        # Increment the level and update the scoreboard
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        # Display "GAME OVER" message at the center
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
