# food.py - Food Class
# This file contains the Food class, which handles the creation and positioning of food items
# for the snake game. The food is a small blue circle that randomly appears on the screen.

from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")  # Set the shape of the food
        self.penup()  # Lift the pen to avoid drawing
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Adjust the size of the food
        self.color("blue")  # Set the color of the food
        self.speed("fastest")  # Set the speed of the food
        self.refresh()  # Move the food to a random position

    def refresh(self):
        random_x = random.randint(-280, 280)  # Generate a random x-coordinate
        random_y = random.randint(-280, 280)  # Generate a random y-coordinate
        self.goto(random_x, random_y)  # Move the food to the new random position
