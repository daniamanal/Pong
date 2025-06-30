from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.bgcolor("Black")
screen.setup(800, 600)
screen.title("Pong")

# Stop screen animations
screen.tracer(0)

# Set up Right and Left Paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Set up the Ball
ball = Ball()

# Setup score
scoreboard = Scoreboard()

# Make Right and Left paddles go Up and Down
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# While the game is on, make the ball move with slower pace
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Ball Needs to Bounce
        ball.bounce_y()

    # Collision with Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect Right Paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect Left Paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Keep displaying screen
screen.exitonclick()
