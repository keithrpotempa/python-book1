from flowers import Flower

class Alstroemeria(Flower):
    
    def __init__(self, color):
        self.name = "Alstroemeria"
        super().__init__(color)