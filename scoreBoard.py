from turtle import Turtle

FONT = ("Arial", 70, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1Score = 0
        self.p2Score = 0
        self.printScores()

    def printScores(self):
        self.reset()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100, 200)
        self.write(self.p1Score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.p2Score, align="center", font=FONT)

    def incrementP1Score(self):
        self.p1Score += 1
        self.printScores()

    def incrementP2Score(self):
        self.p2Score += 1
        self.printScores()

    def isGameOver(self):
        return self.p1Score == 5 or self.p2Score == 5

    def printGameOver(self):
        self.reset()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
