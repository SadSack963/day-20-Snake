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

# List of snake segments: [{turtle, position}]
snake_body = []


def new_seg(index):
    # Create a snake segment
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    snake_body.append({"seg": Turtle(shape="square"), "x": -index * 20, "y": 0})
    snake_body[index]["seg"].speed(1)
    snake_body[index]["seg"].color(color)
    snake_body[index]["seg"].pu()
    pos = (snake_body[index]["x"], snake_body[index]["y"])
    snake_body[index]["seg"].setposition(pos)


def move_snake(head, tail, dir_x, dir_y):
    """To move the snake:
        Make the Tail the new Head with new location depending on direction of movement.
        All other segments remain untouched.
    Requires: index to Head, index to Tail, x axis direction, y axis direction
    Direction x/y should be an integer representing the direction along the axis:
        1: positive, 0: no movement, -1: negative"""
    snake_body[tail]["x"] = snake_body[head]["x"] + (20 * dir_x)
    snake_body[tail]["y"] = snake_body[head]["y"] + (20 * dir_y)
    pos = (snake_body[tail]["x"], snake_body[tail]["y"])
    snake_body[tail]["seg"].setposition(pos)
    new_head = tail



    # THIS IS IT - returns the INDEX to the first lowest item found:
    min_x = min(range(len(snake_body)), key=lambda index: snake_body[index]['x'])
    min_y = min(range(len(snake_body)), key=lambda index: snake_body[index]['y'])
    print(snake_body)
    print(min_x, min_y)


    # if dir_x == 1:
    #     tail = min(seq_x)
    # new_tail =


# Create 3 segment snake
for i in range(0, 3):
    new_seg(i)

time.sleep(2)

# Initialize snake
head_index = 0
tail_index = 2
direction_x = 1
direction_y = 0

# Move snake
move_snake(head=head_index,
           tail=tail_index,
           dir_x=direction_x,
           dir_y=direction_y)


s.exitonclick()
