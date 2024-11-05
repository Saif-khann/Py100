"""
🐢 (Py100: 100 Days of Python Challenge)
Author: Saif Khan
-----------------------------------
Day 23: Turtle Crossing Game
-----------------------------------
Description:
This project simulates a classic Turtle Crossing game. 
The player, represented by a turtle, attempts to cross a road while avoiding moving cars. 
As the player progresses, the game speeds up and becomes more challenging.

Files:
- main.py: Main game loop, initializing objects, and handling screen updates.
- player.py: Handles the player turtle's movement and position.
- car_manager.py: Manages car creation, movement, and speed adjustments.
- scoreboard.py: Manages and displays the player's current level and game over message.
-----------------------------------
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the player, car manager, and scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Set up keyboard listeners
screen.listen()
screen.onkey(player.go_up, "Up")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create and move cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect if player has successfully crossed
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

# Exit the game on click
screen.exitonclick()
