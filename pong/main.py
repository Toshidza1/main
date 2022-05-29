from turtle import Screen
from rocket import Rocket, STARTING_POSITIONS
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

rocket = Rocket()
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(rocket.move_1_up, "Up")
screen.onkey(rocket.move_1_down, "Down")
screen.onkey(rocket.move_2_up, "w")
screen.onkey(rocket.move_2_down, "s")
game_is_on = True
while game_is_on:
    time.sleep(ball.moving_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(rocket.segments[0]) < 40 and ball.xcor() > 350 \
            or ball.distance(rocket.segments[1]) < 40 and ball.xcor() < -350:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.update_left()
        
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.update_right()
  


screen.exitonclick()
