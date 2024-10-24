COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
import random
from turtle import Turtle


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.STARTING_MOVE_DISTANCE = 5


    def create_car(self):

        random_number = random.randint(1, 6)
        if random_number == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(300, random.randint(-250, 250))
            self.all_cars.append(car)

    def move_car(self):

        for car in self.all_cars:
            car.backward(self.STARTING_MOVE_DISTANCE)

    def speed_up(self):
        self.STARTING_MOVE_DISTANCE += MOVE_INCREMENT







