from turtle import Turtle

ALIGNMENT = "center"
FONT = ("monospace", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.pu()
        self.color("black")  
        self.write_score()  
    
    def write_score(self):
        self.clear()
        self.goto(x=-220, y=250)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.goto((0,0))
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)