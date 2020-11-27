from turtle import Screen

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class ScreenSetup:

    def __init__(self):
        self.s = Screen()
        self.s.colormode(255)
        self.s.bgcolor("black")
        self.s.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.s.title("Snake")
        self.s.tracer(0)  # Turn off screen animation
        self.s.listen()  # listen for keystrokes
