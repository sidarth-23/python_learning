from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.tracer(0)

left_paddle = Paddle(350)
right_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.up, "Up")
screen.onkey(left_paddle.down, "Down")
screen.onkey(right_paddle.up, "w")
screen.onkey(right_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() > 320 or ball.distance(right_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    # Detect wall collision
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.left_point()

    # Detect collision with left paddle
    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
