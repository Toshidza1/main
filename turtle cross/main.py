import time
from turtle import Screen, Turtle
from player import Player, FINISH_LINE_Y,STARTING_POSITION
from car_manager import CarManager, cars_list
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score=Scoreboard()
cars= CarManager()
cartman = Player()



screen.listen()
screen.onkeypress(cartman.move, "w")
game_is_on = True
while game_is_on:
    cars.create_cars()
    cars.move_cars()
    time.sleep(0.1)
    screen.update()
    
    for car in cars_list:
        if car.distance(cartman) < 20:
            game_is_on = False
            score.final_score()
    if cartman.ycor() > FINISH_LINE_Y :
        score.score_plus()
        score.update_scoreboard()
        time.sleep(1)
        cartman.goto(STARTING_POSITION)
        score.clear()
        time.sleep(0.1)

screen.exitonclick()
