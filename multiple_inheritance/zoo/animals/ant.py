from movements import IWalking, IDigging
from dwellings import IUndergroundDwelling

class Ant(IWalking, IDigging, IUndergroundDwelling):

    def __init__(self, name):
        IDigging.__init__(self)
        IWalking.__init__(self)
        IUndergroundDwelling.__init__(self)
        self.name = name

    def __str__(self):
        return f'{self.name} the Ant'
