import time
from turtle import Screen , Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard((0, 200))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_is_on = True

while game_is_on: 
    time.sleep(ball.move_speed)  
    screen.update()
    ball.move()

    # defect ball from top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


    #detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_move *= -1

    #detect when right paddle misses
    if ball.xcor() > 380:   
        ball.reset_position()   
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()  
    
    #detect when left paddle misses
    if ball.xcor() < -380:   
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()      


screen.exitonclick()