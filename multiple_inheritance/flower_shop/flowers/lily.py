from flowers import Flower

class Lily(Flower):
    
    def __init__(self, color):
        self.name = "Lily"
        super().__init__(color)