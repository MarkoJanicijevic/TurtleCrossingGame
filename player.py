STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor()
        self.goto(0, new_y+10)

    def back_to_start(self):
        self.goto(STARTING_POSITION)

