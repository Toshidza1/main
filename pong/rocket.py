from turtle import Turtle

STARTING_POSITIONS = [(380, 0), (-380, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Rocket(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_rockets()
    
    def create_rockets(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
        
    def add_segment(self, pos):
        new_square = Turtle(shape="square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(pos)
        new_square.shapesize(stretch_wid=5, stretch_len=1)
        self.segments.append(new_square)
        
    def move_1_up(self):
        new_y = self.segments[0].ycor() + MOVE_DISTANCE
        self.segments[0].goto(self.segments[0].xcor(), new_y)
        
    def move_1_down(self):
        new_y = self.segments[0].ycor() - MOVE_DISTANCE
        self.segments[0].goto(self.segments[0].xcor(), new_y)
        
    def move_2_up(self):
        new_y = self.segments[1].ycor() + MOVE_DISTANCE
        self.segments[1].goto(self.segments[1].xcor(), new_y)
    
    def move_2_down(self):
        new_y = self.segments[1].ycor() - MOVE_DISTANCE
        self.segments[1].goto(self.segments[1].xcor(), new_y)