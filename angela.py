from turtle import Screen
import time
import class_snake
import class_food
import screen
import class_scoreboard
import gameover

# Create the screen
s = screen.ScreenSetup().s

# Create a snake and food
snake = class_snake.Snake()
food = class_food.Food()
scoreboard = class_scoreboard.Scoreboard()

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
    time.sleep(0.2)  # slow down the animation
    snake.move_body()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_food()
        scoreboard.update()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_on = False
        gameover.GameOver()

    # If the head collides with any body segment then trigger game over.
    for seg in snake.body:
        if seg != snake.head and snake.head.distance(seg) < 10:
            game_on = False
            gameover.GameOver()


s.exitonclick()
