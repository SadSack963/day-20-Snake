from turtle import Turtle, Screen
from random import randint
import time

# Screen setup
s = Screen()
s.colormode(255)
s.bgcolor("black")
s.setup(width=600, height=600)
s.title("Snake")

# Turtle setup

# List of snake segments: [{turtle, x position, y position}]
snake_body = []
seg_size = 20


def new_seg(x, y):
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    new_segment = Turtle(shape="square")
    new_segment.speed(1)
    new_segment.color(color)
    new_segment.pu()
    pos = (x, y)
    new_segment.setposition(pos)
    snake_body.append({"seg": new_segment, "x": x, "y": y})


def move_snake(index):
    new_pos_x = snake_body[index-1]["x"]
    new_pos_y = snake_body[index-1]["y"]
    snake_body[index]["x"] = new_pos_x
    snake_body[index]["y"] = new_pos_y
    snake_body[index]["seg"].goto(new_pos_x, new_pos_y)


for i in range(0, -3, -1):
    new_seg(x=(i * seg_size), y=0)


while snake_body[0]["x"] < 280:
    for i in range(len(snake_body) - 1, 0, -1):
        move_snake(i)
    snake_body[0]["seg"].fd(seg_size)
    snake_body[0]["x"] += seg_size
    snake_body[0]["y"] = 0

#     time.sleep(1)  # gives time to view the colours

s.exitonclick()
