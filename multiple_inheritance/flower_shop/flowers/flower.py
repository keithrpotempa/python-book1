class Flower:
  
    def __init__(self, color):
        self.color = color
        self.organic = False
        
    def describe(self):
        print(f"{self.name} is {self.color}")