from flowers import Flower

class Rose(Flower):
    
    def __init__(self, color):
        self.name = "Rose"
        super().__init__(color)