from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# set up the game area
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

# create the game components
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()

#keybindings
screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")


# create the scoreboard
scoreboard = Scoreboard()

game_on = True

while game_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    # ball collision detection with the wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # collision detection with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 330) or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x() 

    # once ball goes past the boundaries, reset and give a point
    if ball.xcor() < -400:
        scoreboard.right_point()
        ball.reset()
    if ball.xcor() > 400:
        scoreboard.left_point()
        ball.reset()


screen.exitonclick()
