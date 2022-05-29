from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.ht()
        self.penup()
        self.update_scoreboard()
        self.clear()
    def update_scoreboard(self):
        self.clear()
        self.write(f"YEEEAH\n score{self.score}", align="center", font=FONT)
        
    def score_plus(self):
        self.score += 1
        
    def final_score(self):
        self.write(f"your score is {self.score}", align="center", font=FONT)
    

