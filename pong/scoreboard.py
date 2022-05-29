from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.ht()
        self.penup()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.l_score, align="left", font=("Courier", 40, "normal"))
        self.goto(100, 230)
        self.write(self.r_score, align="left", font=("Courier", 40, "normal"))
    
    def update_right(self):
        self.r_score += 1
        self.update_scoreboard()
    def update_left(self):
        self.l_score += 1
        self.update_scoreboard()
        
    def difficult_up(self):
        self.clear()
        self.goto(0,230)
        self.write("UP TEMPO", align="center",font=("Courier", 50, "normal"))