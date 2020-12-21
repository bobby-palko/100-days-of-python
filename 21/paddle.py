from turtle import Turtle

UP = 90
DOWN = 270

MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, coords=(0, 0)):
        super().__init__()  
        self.shape("square") 
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.pu()
        self.goto(coords)


    def up(self):
        self.goto((self.xcor(), self.ycor() + MOVE_DISTANCE))

    def down(self):
        self.goto((self.xcor(), self.ycor() - MOVE_DISTANCE))