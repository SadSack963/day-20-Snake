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


def new_seg(x, y):
    # Create a snake segment
    # Each segment is size 20 x 20
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    new_segment = Turtle(shape="square")
    new_segment.speed(1)
    new_segment.color(color)
    new_segment.pu()
    pos = (x, y)
    new_segment.setposition(pos)
    snake_body.append({"seg": new_segment, "x": x, "y": y})


def min_max_index(dir_x, dir_y):
    """    Requires: x axis direction, y axis direction
    Returns: the INDEX to the (first) lowest/highest item found,
    depending upon which direction is relevant."""
    if dir_x > 0:
        return min(range(len(snake_body)), key=lambda index: snake_body[index]['x'])
    elif dir_x < 0:
        return max(range(len(snake_body)), key=lambda index: snake_body[index]['x'])
    elif dir_y > 0:
        return min(range(len(snake_body)), key=lambda index: snake_body[index]['y'])
    elif dir_y < 0:
        return max(range(len(snake_body)), key=lambda index: snake_body[index]['y'])
    else:
        return 0


def move_snake(head, tail, dir_x, dir_y):
    """
    To move the snake:
        Make the Tail the new Head with new location depending on direction of movement.
        All other segments remain untouched.
    Requires: index to Head, index to Tail, x axis direction, y axis direction
    Direction x/y should be an integer representing the direction along the axis:
        1: positive, 0: no movement, -1: negative
    Returns: index of new Head, index of new Tail
    """
    snake_body[tail]["x"] = snake_body[head]["x"] + (20 * dir_x)
    snake_body[tail]["y"] = snake_body[head]["y"] + (20 * dir_y)
    pos = (snake_body[tail]["x"], snake_body[tail]["y"])
    snake_body[tail]["seg"].setposition(pos)
    new_head = tail
    new_tail = min_max_index(dir_x, dir_y)
    return new_head, new_tail


# START
# =====

# Create a 3 segment snake with the head at (0, 0)
# and facing along the positive x axis
for i in range(0, 3):
    new_seg(i * -20, 0)

time.sleep(1)  # gives time to view the colours

# Initialize snake
head = 0
tail = 2
direction_x = 0
direction_y = 1

game_running = True

while game_running:
    if snake_body[head]["x"] > 260 or snake_body[head]["y"] > 260:
        game_running = False
    else:
        # Move snake
        result = move_snake(
            head=head,
            tail=tail,
            dir_x=direction_x,
            dir_y=direction_y
        )
        head = result[0]
        tail = result[1]
        time.sleep(1)  # gives time to view the colours

s.exitonclick()

# ------------------------------------------------------------------------------

# Aborted this method of moving the snake without modifying the list.

# A much simpler way is to add a new element at snake_body[0]
# and remove the last element in the list.

# I was attempting to avoid this because of the extra computation
# required to move the entire list when inserting an element at position 0,
# but it became too cumbersome to determine which element was last in the chain.

# See https://simplegametutorials.github.io/love/snake/

