from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# positional constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0 

class Snake:

    def __init__(self):

        # each piece of the snake will be its own turtle object stored in a list for state management
        self.segments = []

        # create the initial length of 3 for the snake
        for position in STARTING_POSITIONS:
            self.add_segment(position)

        self.head = self.segments[0]

    def move(self):
        """Moves the snake forward in the direction its facing by 1 block length"""

        # move our snake from tail to head.
        # this prevents "gaps" by pulling the head away from the body
        # it also allows the body to follow the head since each piece moves to the
        # position of the pice ahead of it in the segments list
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)        

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.pu()
        turtle.goto(position)
        self.segments.append(turtle)
        
