from turtle import Turtle
from random import randint
from screen import SCREEN_WIDTH, SCREEN_HEIGHT


class Food(Turtle):
    # Food inherits all attributes and methods from Turtle
    def __init__(self):
        super().__init__()  # Call the Turtle initializer
        self.shape("circle")
        self.color("green")
        self.speed("fastest")
        self.pu()
        self.resizemode("user")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # circle will be scaled to 50%: 10 x 10
        self.new_food()

    def new_food(self):
        rand_x = randint(-int(SCREEN_WIDTH / 2.15), int(SCREEN_WIDTH / 2.15))  # roughly +/- 280
        rand_y = randint(-int(SCREEN_HEIGHT / 2.15), int(SCREEN_HEIGHT / 2.15))
        self.goto(rand_x, rand_y)
