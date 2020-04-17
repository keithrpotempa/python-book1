from movements import IDigging, ISlithering
from dwellings import IUndergroundDwelling

class Earthworm(IDigging, ISlithering, IUndergroundDwelling):

    def __init__(self, name):
        IDigging.__init__(self)
        ISlithering.__init__(self)
        IUndergroundDwelling.__init__(self)
        self.name = name

    def __str__(self):
        return f'{self.name} the Earthworm'
