from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()

colors = [(245, 245, 244), (226, 234, 243), (131, 164, 204), (228, 149, 99), (30, 44, 64), (238, 245, 242), (245, 234, 238), (166, 58, 48), (202, 135, 147), (237, 212, 85), (41, 101, 150), (135, 183, 161), (150, 62, 71), (52, 42, 45), (159, 33, 31), (219, 82, 73), (238, 165, 155), (58, 117, 99), (60, 49, 45), (173, 29, 31), (231, 163, 168), (35, 61, 56), (15, 96, 71), (33, 60, 107), (170, 188, 222), (188, 101, 111), (104, 126, 161), (14, 85, 109), (174, 200, 188), (33, 151, 211)]

screen.colormode(255)

turtle.pu()
turtle.hideturtle()
turtle.speed(0)
turtle.setpos(-100, -100)

def make_row():
    position = turtle.pos()
    for _ in range(10):
        turtle.dot(20, random.choice(colors))
        turtle.fd(50)
    turtle.setpos(position[0], position[1] + 50)

for _ in range(10):
    make_row()

screen.exitonclick()