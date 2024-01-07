from turtle import Turtle

P1POSITION = [(-280, 0), (-280, -20), (-280, -40)]
P2POSITION = [(280, 0), (280, -20), (280, -40)]


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.positions = P1POSITION if self.side == "right" else P2POSITION
        self.segments = []
        self.createPaddle()
        self.head = self.segments[0]

    def createPaddle(self):
        for i in self.positions:
            self.addSegment(i)

    def addSegment(self, postion):
        x, y = postion
        newSegment = Turtle("square")
        newSegment.penup()
        newSegment.color("white")
        newSegment.goto(x, y)
        self.segments.append(newSegment)

    # Movement Control
    def move(self):
        for segIdx in range(len(self.segments) - 1, 0, -1):
            x, y = self.segments[segIdx - 1].pos()
            self.segments[segIdx].goto(x, y)
        self.head.forward(20)

    def up(self):
        self.head.setheading(90)
        self.move()

    def down(self):
        self.head.setheading(270)
        self.move()
