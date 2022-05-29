class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("123123")

class Fish(Animal):
    def __init__(self):
        super().__init__()