from movements import IFlying
from dwellings import ISkyDwelling

class Parakeet(IFlying, ISkyDwelling):

    def __init__(self, name):
        IFlying.__init__(self)
        ISkyDwelling.__init__(self)
        self.name = name

    def __str__(self):
        return f'{self.name} the Parakeet'
