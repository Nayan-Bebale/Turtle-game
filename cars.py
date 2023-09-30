from turtle import Turtle
import random

COLORS = ["red", "green", "yellow", "pink", "blue", "light pink", "orange"]
MOVE_CARS = 5
MOVE_INCREASE = 10


class Cars:
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_CARS

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_cars = Turtle()
            y_position = random.randint(-230, 230)
            new_cars.shape("square")
            new_cars.shapesize(stretch_wid=1, stretch_len=2)
            new_cars.penup()
            new_cars.color(random.choice(COLORS))
            new_cars.goto(x=400, y=y_position)
            self.all_cars.append(new_cars)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREASE
