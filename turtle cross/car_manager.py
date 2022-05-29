from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SPEED = ["fastest", "fast", "normal", "slow", "slowest"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# y_pos = range(-200, 700, random.choice(range(20,100)))
# x_pos = range(200,350, random.choice(range(50, 300)))

cars_list =[]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        # self.cars = []
        self.hideturtle()
        self.create_cars()
        self.move_cars()
        
    def create_cars(self):
            random_chance= random.randint(1, 6)
            if random_chance == 1:
                y_pos = range(-230, 260, random.choice(range(90, 100)))
                x_pos = range(310, 350, random.choice(range(50, 300)))
                new_car = Turtle("square")
                new_car.speed(random.choice(SPEED))
                new_car.shapesize(stretch_len=1.5, stretch_wid=1)
                new_car.color(random.choice(COLORS))
                new_car.penup()
                new_car.goto(x=random.choice(x_pos),y=random.choice(y_pos))
                cars_list.append(new_car)
    
    def move_cars(self):
        for car in cars_list:
            car.back(STARTING_MOVE_DISTANCE)
            


