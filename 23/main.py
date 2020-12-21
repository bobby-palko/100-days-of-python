from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# set up the game area
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    # detect collision with food and update the score
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if (snake.head.xcor() > 295 or snake.head.xcor() < -295) or (snake.head.ycor() > 295 or snake.head.ycor() < -295):
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
    
    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over
            scoreboard.reset()
            snake.reset()

screen.exitonclick()