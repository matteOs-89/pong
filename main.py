from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

paddle = Turtle()
screen = Screen()
score = ScoreBoard()



screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("OS PONG GAME")
screen.tracer(0)

pad_r = Paddle((350, 0))
pad_l = Paddle((-350, 0))


screen.listen()
screen.onkey(pad_r.go_up, "Up")
screen.onkey(pad_r.go_down, "Down")

screen.onkey(pad_l.go_up, "w")
screen.onkey(pad_l.go_down, "s")

ball = Ball(1)

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(pad_r) < 50 and ball.xcor() > 330 or ball.distance(pad_l) < 50 and ball.xcor() > -340:
        ball.bounce_x()

    #resetting and add scores for the left side

    if ball.xcor() > 370:
        ball.reset_position()
        score.l_point()
        score.update_score()




    #resetting and adding score for right side
    if ball.xcor() < -370:
        ball.reset_position()
        score.r_point()
        score.update_score()



























screen.exitonclick()