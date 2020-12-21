from turtle import Turtle
import random

STARTING_SPEED = 5
SPEED_INCREASE = 10

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager:
    
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_SPEED

    def new_car(self):
        generation_chance = random.randint(1,6)
        if generation_chance == 1:
            car = Turtle()
            car.pu()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            car.goto(300, rand_y)
            car.setheading(180)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def faster(self):
        self.car_speed += SPEED_INCREASE
