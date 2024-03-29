from time import sleep
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard

# Setup Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Pong")

# Create instances
player1 = Paddle((-350, 0))
player2 = Paddle((350, 0))
ball = Ball()
scoreBoard = ScoreBoard()

# Listen for keystrokes
screen.listen()
# Control for player 1
screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")
# Control for player 2
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")

# Game loop
isGameOn = True
while isGameOn:
    screen.update()
    sleep(ball.currentSpeed)
    ball.move()

    # Detect wall collsions for ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    # Detect collsion with paddle
    if (ball.xcor() > 330 and ball.distance(player2) < 40) or (
        ball.xcor() < -330 and ball.distance(player1) < 40
    ):
        ball.bounceX()
        ball.currentSpeed *= 0.9

    # player misses
    if ball.xcor() > 380:
        scoreBoard.incrementP1Score()
        ball.resetPos()

    if ball.xcor() < -380:
        scoreBoard.incrementP2Score()
        ball.resetPos()
    if scoreBoard.isGameOver():
        scoreBoard.printGameOver()
        isGameOn = False

screen.exitonclick()
