from time import sleep
from turtle import Screen
from paddle import Paddle

# Setup Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Pong")

# Create instances
player1 = Paddle("right")
player2 = Paddle("left")

# Listen for keystrokes
screen.listen()
# Control for player 1
screen.onkey(player1.up, "Up")
screen.onkey(player1.down, "Down")
# Control for player 2
screen.onkey(player2.up, "w")
screen.onkey(player2.down, "s")

# Game loop
isGameOn = True
while isGameOn:
    screen.update()
    sleep(0.1)


screen.exitonclick()
