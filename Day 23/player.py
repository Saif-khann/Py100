from turtle import Turtle

# Constants for player's position and movement
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()  # Place player at the starting position
        self.setheading(90)  # Face upwards

    def go_up(self):
        # Move player upwards by a set distance
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        # Move player back to the starting position
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        # Check if player has crossed the finish line
        return self.ycor() > FINISH_LINE_Y
