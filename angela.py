from turtle import Turtle, Screen
from random import randint
import time
import class_snake


def get_direction():
    global current_direction

    s.onkey(snake.left, "left")
    # if ? and current_direction != "right":
    #     current_direction = snake.left()
    s.onkey(snake.right, "right")
    # if ? and current_direction != "left":
    # current_direction = snake.right()
    s.onkey(snake.up, "up")
    # if ? and current_direction != "down":
    # current_direction = snake.up()
    s.onkey(snake.down, "down")
    # if ? and current_direction != "up":
    # current_direction = snake.down()


# Screen setup
s = Screen()
s.colormode(255)
s.bgcolor("black")
s.setup(width=600, height=600)
s.title("Snake")
s.tracer(0)  # Turn off screen animation

# Create a snake
snake = class_snake.Snake()
current_direction = ""

s.listen()  # listen for keystrokes
# turtle.onkey(fun, key):
#   fun – a function WITH NO ARGUMENTS, or None
#   key – a string: key (e.g. “a”) or key-symbol (e.g. “space”)
#   Tkinter Key Symbols are at https://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")


# while -280 < snake.head.xcor() < 280 \
#         and -280 < snake.head.ycor() < 280:
while True:
    s.update()  # update the screen
    time.sleep(0.1)  # slow down the animation
    snake.move_body()

s.exitonclick()
