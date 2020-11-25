from turtle import Turtle, Screen
from random import randint


# Screen setup
s = Screen()
s.colormode(255)
s.bgcolor("black")
s.setup(width=600, height=600)
s.title("Snake")


# Turtle setup

# List of snake segments: [{turtle, position}]
snake_body = []


def new_seg(index):
    # Create a snake segment
    snake_body.append({"seg": Turtle(shape="square"), "pos": (-index * 20, 0)})
    snake_body[index]["seg"].speed(1)
    snake_body[index]["seg"].color("white")
    snake_body[index]["seg"].setposition(snake_body[index]["pos"])


for i in range(0, 3):
    new_seg(i)

# To move the snake:
#   insert the last tail segment as the new head at the first segment and with a new position
#   then remove the last segment
#   All other segments remain untouched


s.exitonclick()
