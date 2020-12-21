from turtle import Turtle

ALIGNMENT = "center"
FONT = ("monospace", 30, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.pu()
        self.color("white")  
        self.write_score()  
    
    def write_score(self):
        self.clear()
        self.goto(x=-100, y=240)
        self.write(f"{self.left_score}", align=ALIGNMENT, font=FONT)
        self.goto(x=100, y=240)
        self.write(f"{self.right_score}", align=ALIGNMENT, font=FONT)
        
    def right_point(self):
        self.right_score += 1
        self.write_score()
    
    def left_point(self):
        self.left_score += 1
        self.write_score()