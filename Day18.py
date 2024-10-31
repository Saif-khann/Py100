'''
🖌 (Py100: 100 Days of Python Challenge)
Author: Saif Khan
-----------------------------------
Day 18: Hirst Painting Project - Python Turtle Graphics
-----------------------------------
Description:
This project simulates a painting inspired by the dot style of artist Damien Hirst.
It uses Turtle graphics to create a grid of randomly colored dots.
The color list was generated to resemble a variety of tones and shades for visual interest.
-----------------------------------
'''

import turtle as turtle_module
import random

# Set the turtle graphics module to use RGB mode for color selection
turtle_module.colormode(255)

# Initialize the turtle (tim) and set its speed, visibility, and position
tim = turtle_module.Turtle()
tim.speed("fastest")       # Set the turtle's drawing speed to the fastest
tim.penup()                # Lift the pen so it doesn't draw while moving
tim.hideturtle()           # Hide the turtle cursor for a clean look

# List of RGB colors for dot colors
color_list = [
    (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135),
    (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185),
    (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
    (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77),
    (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90),
    (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
    (107, 127, 153), (174, 94, 97), (176, 192, 209)
]

# Initial position setup
tim.setheading(225)      # Move the turtle at an angle to start the grid from the bottom left
tim.forward(300)         # Move the turtle to a position to start drawing the grid
tim.setheading(0)        # Set the turtle to face right for dot placement

# Number of dots to create in the painting
number_of_dots = 100

# Loop to create each dot in the grid
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))   # Draw a dot with a random color from color_list
    tim.forward(50)                          # Move forward to position for the next dot

    # After every 10 dots, move up to the next row and reset to the left side of the grid
    if dot_count % 10 == 0:
        tim.setheading(90)                   # Face up to move to the next row
        tim.forward(50)                      # Move up one row
        tim.setheading(180)                  # Face left to return to the start of the row
        tim.forward(500)                     # Move to the beginning of the next row
        tim.setheading(0)                    # Face right to start drawing dots again

# Exit the screen when clicked
screen = turtle_module.Screen()
screen.exitonclick()