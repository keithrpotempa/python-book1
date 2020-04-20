from movements import IDigging, ISlithering, ISwimming
from dwellings import IUndergroundDwelling

class TimberRattlesnake(IDigging, ISlithering, ISwimming, IUndergroundDwelling):

    def __init__(self, name):
        IDigging.__init__(self)
        ISlithering.__init__(self)
        ISwimming.__init__(self)
        IUndergroundDwelling.__init__(self)
        self.name = name

    def __str__(self):
        return f'{self.name} the Timber Snake'
