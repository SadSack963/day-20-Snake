from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.pu()
        self.color("white")
        self.setposition(0, 280)
        self.score = -1
        self.update()

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, "normal"))
