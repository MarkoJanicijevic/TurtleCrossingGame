FONT = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_level = 1
        self.hideturtle()
        self.penup()

        self.color("white")
        self.update_scoreboard()


    def level_up(self):
        self.starting_level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 280)
        self.write(f"Level {self.starting_level} ", FONT)

    def game_over(self):
        self.gameover = Turtle()
        self.gameover.hideturtle()
        self.gameover.penup()
        self.gameover.goto(0, 0)
        self.gameover.color("white")
        self.gameover.write("Game over! ", FONT)

