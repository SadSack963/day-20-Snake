from turtle import Turtle


class Scoreboard:

    def __init__(self):
        self.sb = Turtle()
        self.sb.hideturtle()
        self.sb.pu()
        self.sb.color("white")
        self.sb.setposition(0, 280)

    def write_score(self, score):
        self.sb.clear()
        self.sb.write(f"Score: {score}", align = "center", font=("Arial", 10, "normal"))
