from flowers import Flower

class Daisy(Flower):
    
    def __init__(self, color):
        self.name = "Daisy"
        super().__init__(color)