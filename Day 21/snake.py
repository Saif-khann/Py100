# snake.py - Snake Class
# This file contains the Snake class, which manages the behavior and movement of the snake.
# The snake is made up of segments that follow each other, and it can move, grow, and change
# direction based on user input.

from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions of the snake segments
MOVE_DISTANCE = 20  # Distance the snake moves per step
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []  # List to store the snake's segments
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # The head of the snake

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)  # Add each segment to the snake

    def add_segment(self, position):
        new_segment = Turtle("square")  # Create a new segment
        new_segment.color("white")  # Set the color to white
        new_segment.penup()  # Lift the pen to avoid drawing
        new_segment.goto(position)  # Move the segment to the specified position
        self.segments.append(new_segment)  # Add the segment to the list

    def extend(self):
        self.add_segment(self.segments[-1].position())  # Add a new segment to the end of the snake

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the previous segment
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the previous segment
            self.segments[seg_num].goto(new_x, new_y)  # Move the segment to the new position
        self.head.forward(MOVE_DISTANCE)  # Move the head forward

    def up(self):
        if self.head.heading() != DOWN:  # Prevent the snake from going in the opposite direction
            self.head.setheading(UP)  # Set the heading to UP

    def down(self):
        if self.head.heading() != UP:  # Prevent the snake from going in the opposite direction
            self.head.setheading(DOWN)  # Set the heading to DOWN

    def left(self):
        if self.head.heading() != RIGHT:  # Prevent the snake from going in the opposite direction
            self.head.setheading(LEFT)  # Set the heading to LEFT

    def right(self):
        if self.head.heading() != LEFT:  # Prevent the snake from going in the opposite direction
            self.head.setheading(RIGHT)  # Set the heading to RIGHT
