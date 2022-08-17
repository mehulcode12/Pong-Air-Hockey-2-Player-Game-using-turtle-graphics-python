from turtle import *
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.bgcolor('grey')
screen.setup(width=800, height=600)
screen.title("Mehul Pong Game - created on 17/08/22")
screen.tracer(0)

ok = Turtle()
def copyright():
    ok.penup()
    ok.goto(x = -375, y = 275)
    ok.write("github.com/mehulcode12", font=("Courier", 10, "normal"))
copyright()

right_paddle = Paddle((375,0))
left_paddle = Paddle((-375,0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(right_paddle.go_up, "o")
screen.onkey(right_paddle.go_down, "l")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #collision with right_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 350:
        ball.bounce_x()
    if ball.distance(left_paddle) < 50 and ball.xcor() > -350:
        ball.bounce_x()

    #detect right paddle misses
    if ball.xcor() > 410:
        ball.reset_position()
        score.left_point()
    
    #detect left paddle misses
    if ball.xcor() < -410:
        ball.reset_position()
        score.right_point()


screen.exitonclick()