from turtle import Turtle

SEG_SIZE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = -90

class Snake:

    def __init__(self):
        self.body = []  # List of snake segments: [Turtle()]
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        """Create 3 segment snake with the Head at (0, 0) and the Tail at (-40, 0)"""
        for i in range(0, -3, -1):
            self.new_seg(x=(i * SEG_SIZE), y=0)

    def new_seg(self, x, y):
        """Create new snake segment at the given position on the screen"""
        new_segment = Turtle(shape="square")
        new_segment.speed(1)
        new_segment.color("white")
        new_segment.pu()
        new_segment.setheading(0)
        new_segment.setposition(x, y)
        self.body.append(new_segment)

    def move_seg(self, index):
        """Move a snake segment to the same position as the previous segment in the chain."""
        new_x = self.body[index - 1].xcor()  # get x coordinate
        new_y = self.body[index - 1].ycor()  # get y coordinate
        self.body[index].goto(new_x, new_y)

    def move_body(self):
        """Move the entire snake body"""
        for i in range(len(self.body) - 1, 0, -1):
            self.move_seg(i)
        self.head.fd(SEG_SIZE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
