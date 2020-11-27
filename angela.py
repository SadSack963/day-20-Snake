from turtle import Screen
import time
import class_snake
import class_food
import screen


# Create the screen
s = screen.ScreenSetup().s

# Create a snake and food
snake = class_snake.Snake()
food = class_food.Food()


# turtle.onkey(fun, key):
#   fun – a function WITH NO ARGUMENTS, or None
#   key – a string: key (e.g. “a”) or key-symbol (e.g. “space”)
#   Tkinter Key Symbols are at https://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")

game_on = True
# while -280 < snake.head.xcor() < 280 \
#         and -280 < snake.head.ycor() < 280:
while game_on:
    s.update()  # update the screen
    time.sleep(0.1)  # slow down the animation
    snake.move_body()

s.exitonclick()
