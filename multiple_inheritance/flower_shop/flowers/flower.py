class Flower:
  
    def __init__(self, color):
        self.color = color
        self.organic = False
        
    def __str__(self):
        print(f"{self.color} {self.name}")