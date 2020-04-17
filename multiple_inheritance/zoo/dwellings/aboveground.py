from containers import Cage

class IAboveGroundDwelling:
    def __init__(self):
        self.container = Cage
        
    def stow_away(self):
        self.container.instances[0].animals.add(self)
        print(f"{self} added to {self.container.instances[0]}")