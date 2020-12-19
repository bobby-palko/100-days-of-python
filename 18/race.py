from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.colormode(1)


is_racing = False

user_bet = screen.textinput(title="Make Your Bets!", prompt="Which turtle will win the race? Enter a color: ")



colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-75, -45, -15, 15, 45, 75]
turtles = []


for i in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.pu()
    turtle.goto(x=-230, y=y_pos[i])
    turtles.append(turtle)

if user_bet:
    is_racing = True

while is_racing:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_racing = False
            if user_bet == winner:
                print(f"You won! The winning turtle was {winner}.")
            else:
                print(f"You lost! The winning turtle was {winner}.")
        dist = random.randint(0, 10)
        turtle.forward(dist)



screen.exitonclick()