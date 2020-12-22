import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.pu()
t.hideturtle()
FONT=("Arial", 8, "normal")

data = pandas.read_csv("50_states.csv")

def write_state(answer):
    row = data[data["state"] == answer]
    t.goto(int(row.x), int(row.y))
    t.write(answer, align="center", font=FONT)


score = 0

while score < 50:
    answer = screen.textinput(title=f"Guess the State: {score}/50", prompt="What's another state's name?").title()

    if answer in data.values:
        score += 1
        write_state(answer)

turtle.mainloop()
