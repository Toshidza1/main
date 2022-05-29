from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.color("green")
        self.speed("fast")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.fd(MOVE_DISTANCE)
        # self.back(MOVE_DISTANCE)

    def collision(self):
        pass
    
    
    
