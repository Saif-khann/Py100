from turtle import Turtle

# Scoreboard class to manage the score display and updates in the Pong game
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")  # Set scoreboard text color to white
        self.penup()  # Lift the pen to prevent drawing
        self.hideturtle()  # Hide the turtle shape
        self.l_score = 0  # Initialize the left player's score
        self.r_score = 0  # Initialize the right player's score
        self.update_scoreboard()  # Display the initial score

    # Update the scoreboard with the current scores
    def update_scoreboard(self):
        self.clear()  # Clear the previous score
        self.goto(-100, 200)  # Position for the left player's score
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)  # Position for the right player's score
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    # Add a point to the left player's score and update the scoreboard
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    # Add a point to the right player's score and update the scoreboard
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
