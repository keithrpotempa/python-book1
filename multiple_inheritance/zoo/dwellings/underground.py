from containers import Hutch

class IUndergroundDwelling:
    def __init__(self):
        self.container = Hutch
        
    def stow_away(self):
        self.container.instances[0].animals.add(self)
        print(f"{self} added to {self.container.instances[0]}")