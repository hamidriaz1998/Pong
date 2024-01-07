from turtle import Turtle

P1POSITION = [(-280, 0), (-280, -20), (-280, -40)]
P2POSITION = [(280, 0), (280, -20), (280, -40)]


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.createPaddle()

    def createPaddle(self):
        for i in P1POSITION if self.side == "left" else P2POSITION:
            self.addSegment(i)

    def addSegment(self, postion):
        x, y = postion
        newSegment = Turtle("square")
        newSegment.penup()
        newSegment.color("white")
        newSegment.goto(x, y)
        self.segments.append(newSegment)
