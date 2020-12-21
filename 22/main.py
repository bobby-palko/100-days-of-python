from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# initialize objects
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.cross_street, "Up")

game_is_running = True

while game_is_running:
    time.sleep(0.1)
    screen.update()

    car_manager.new_car()

    car_manager.move_cars()

    # detect when the player reaches the top of the screen
    if player.ycor() > 280:
        player.reset()
        scoreboard.increase_level()
        car_manager.faster()

    # detect when turtle collides with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_running = False
            scoreboard.game_over()

screen.exitonclick()