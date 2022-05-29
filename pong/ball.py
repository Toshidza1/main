from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed("fastest")
        self.score = [0, 0]
        self.moving_speed = 0.1
        self.refresh()
        self.x_move = 10
        self.y_move = 10
    
    def refresh(self):
        random_x = random.randint(-350, 350)
        random_y = random.randint(-280, 280)
        self.setposition(random_x, random_y)
        self.moving_speed = 0.1
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        self.moving_speed *= 0.9
