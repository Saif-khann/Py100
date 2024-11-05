from turtle import Turtle
import random

# Constants for car properties and movement
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.all_cars = []  # List to store all car objects
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial speed of cars

    def create_car(self):
        # Create a new car with a 1 in 6 chance
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        # Move each car backward by the current speed
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        # Increase car speed as player progresses
        self.car_speed += MOVE_INCREMENT
