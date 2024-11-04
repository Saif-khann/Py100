from turtle import Turtle

# Ball class to handle the ball's properties and movements in the Pong game
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")  # Set the ball color to white
        self.shape("circle")  # Set the ball shape to a circle
        self.penup()  # Lift the pen to prevent drawing on the screen
        self.x_move = 7  # Initial movement in the x-direction
        self.y_move = 7  # Initial movement in the y-direction
        self.move_speed = 0.1  # Control the speed of the ball

    # Move the ball to a new position based on x_move and y_move
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)  # Move the ball to the new position

    # Reverse the ball's y-direction when it hits the top or bottom walls
    def bounce_y(self):
        self.y_move *= -1

    # Reverse the ball's x-direction when it hits a paddle, and speed up
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # Increase the ball's speed by reducing sleep time

    # Reset the ball to the center and reset the speed
    def reset_position(self):
        self.goto(0, 0)  # Move the ball to the center
        self.move_speed = 0.1  # Reset the speed to the original value
        self.bounce_x()  # Reverse the ball's direction to start moving in the opposite way
