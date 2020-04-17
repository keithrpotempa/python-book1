from containers import Aviary

class ISkyDwelling:
    def __init__(self):
        self.container = Aviary
        
    def stow_away(self):
        self.container.instances[0].animals.add(self)
        print(f"{self} added to {self.container.instances[0]}")