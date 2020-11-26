from turtle import Turtle, Screen
from random import randint
import time

# Screen setup
s = Screen()
s.colormode(255)
s.bgcolor("black")
s.setup(width=600, height=600)
s.title("Snake")
s.tracer(0)  # Turn off screen animation


# Turtle setup
# List of snake segments: [Turtle()]
snake_body = []
seg_size = 20


def new_seg(x, y):
    new_segment = Turtle(shape="square")
    new_segment.speed(1)
    new_segment.color("white")
    new_segment.pu()
    new_segment.setposition(x, y)
    snake_body.append(new_segment)


def move_snake(index):
    new_pos_x = snake_body[index-1].xcor()  # get x coordinate
    new_pos_y = snake_body[index-1].ycor()  # get y coordinate
    snake_body[index].goto(new_pos_x, new_pos_y)


# Create 3 segment snake
for i in range(0, -3, -1):
    new_seg(x=(i * seg_size), y=0)
    s.update()

while snake_body[0].xcor() < 280:
    for i in range(len(snake_body) - 1, 0, -1):
        move_snake(i)
    snake_body[0].fd(seg_size)
    s.update()
    time.sleep(0.5)  # slow down the animation

#     time.sleep(1)  # gives time to view the colours

s.exitonclick()
