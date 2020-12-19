from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def move_fwd():
    t.forward(10)

def move_bkwd():
    t.back(10)

def turn_clockwise():
    t.left(10)

def turn_counter_clockwise():
    t.right(10)

def clear():
    t.clear()
    t.reset()

s.listen()

# keybindings
s.onkey(key="w", fun=move_fwd)
s.onkey(key="s", fun=move_bkwd)
s.onkey(key="a", fun=turn_counter_clockwise)
s.onkey(key="d", fun=turn_clockwise)
s.onkey(clear, "c")

s.exitonclick()