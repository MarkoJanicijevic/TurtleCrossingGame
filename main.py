import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
#car_manager.create_car()
screen.listen()
screen.onkeypress(player.move, "Up")

# car_manager.create_car(300)

game_is_on = True

scoreboard = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()


    if player.ycor() == 280:
        player.back_to_start()
        scoreboard.level_up()
        car_manager.speed_up()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()