from turtle import Turtle

# Constants for the starting positions and movement settings
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions of the snake segments
MOVE_DISTANCE = 20  # Distance the snake moves with each step
UP = 90  # Angle for upward movement
DOWN = 270  # Angle for downward movement
LEFT = 180  # Angle for leftward movement
RIGHT = 0  # Angle for rightward movement

class Snake:

    def __init__(self):
        self.segments = []  # List to store the snake segments
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # The first segment is the head of the snake

    def create_snake(self):
        """Create the snake with three segments at the starting positions."""
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")  # Each segment is a square-shaped turtle
            new_segment.color("white")  # Set the segment color to white
            new_segment.penup()  # Lift the pen to prevent drawing lines
            new_segment.goto(position)  # Move the segment to the given position
            self.segments.append(new_segment)  # Add the segment to the snake

    def move(self):
        """Move the snake forward by updating each segment's position."""
        # Move each segment to the position of the segment in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the segment in front
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the segment in front
            self.segments[seg_num].goto(new_x, new_y)  # Move the segment to the new position
        self.head.forward(MOVE_DISTANCE)  # Move the head forward

    def up(self):
        """Change the snake's direction to up if it's not currently moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the snake's direction to down if it's not currently moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change the snake's direction to left if it's not currently moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change the snake's direction to right if it's not currently moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
