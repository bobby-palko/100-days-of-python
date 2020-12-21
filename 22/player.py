from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVE_SPEED = 10
FINISH = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.setheading(90)
        self.reset()

    def cross_street(self):
        self.forward(MOVE_SPEED)

    def reset(self):
        self.goto(STARTING_POSITION)