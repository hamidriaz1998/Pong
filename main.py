from turtle import Screen

# Setup Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Pong")

# Listen for keystrokes
screen.listen()
# Control for player 2
screen.onkey("Up")
screen.onkey("Down")
# Control for player 2
screen.onkey("W")
screen.onkey("S")


screen.exitonclick()
