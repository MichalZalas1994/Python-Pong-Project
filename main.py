from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



# Create new screen which is an object from class turtle
screen = Screen()
# Setting setup for the screen object
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Pong game!")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
ball_speed = 0.1
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# the while loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 400:
        ball.ball_reset_position()
        scoreboard.l_point()

    # Detect left paddle misses
    if ball.xcor() < -400:
        ball.ball_reset_position()
        scoreboard.r_point()

# At the very end, user closes the screen on click
screen.exitonclick()
