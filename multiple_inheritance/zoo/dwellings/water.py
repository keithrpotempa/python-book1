from containers import FishBowl

class IWaterDwelling:
    def __init__(self):
        self.container = FishBowl
        
    def stow_away(self):
        self.container.instances[0].animals.add(self)
        print(f"{self} added to {self.container.instances[0]}")