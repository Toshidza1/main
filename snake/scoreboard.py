from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 260)
        self.refresh_scoreboard()
        # self.write(f"score: {self.score} ", False, align="center", font=("Courier", 19, "normal"))
    
    def refresh_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} High score: {self.high_score} ", False, align="center", font=("Courier", 19, "normal"))

    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.refresh_scoreboard()
    
    # def end_game(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", False, align="center", font=("Courier", 19, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.refresh_scoreboard()