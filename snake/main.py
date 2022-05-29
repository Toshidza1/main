from turtle import Screen
from snake import Snake
from food import Food

from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # food collision

    if snake.head.distance(food) < 15:
        scoreboard.refresh_scoreboard()
        snake.extend()
        scoreboard.increase_score()
        food.refresh()
        for n in snake.segments:
            if n.distance(food) == 0:
                food.refresh()
    # wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    # tail collision
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()
    


screen.exitonclick()
