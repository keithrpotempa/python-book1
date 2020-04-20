from flowers import Flower

class Poppy(Flower):
    
    def __init__(self, color):
        self.name = "Poppy"
        super().__init__(color)