from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.moveX = 10
        self.moveY = 10

    def move(self):
        self.goto(self.xcor() + self.moveX, self.ycor() + self.moveY)

    def bounceX(self):
        self.moveX *= -1

    def bounceY(self):
        self.moveY *= -1

    def resetPos(self):
        self.goto(0, 0)
        self.bounceX()
