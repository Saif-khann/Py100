from turtle import Turtle

# Paddle class to create and control paddles in the Pong game
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")  # Set paddle shape to a square
        self.color("white")  # Set paddle color to white
        self.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the shape to make it a paddle
        self.penup()  # Lift the pen to prevent drawing
        self.goto(position)  # Move the paddle to the specified position

    # Move the paddle up by 20 pixels
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)  # Update the paddle's y-coordinate

    # Move the paddle down by 20 pixels
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)  # Update the paddle's y-coordinate
