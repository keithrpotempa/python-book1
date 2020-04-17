from movements import ISwimming
from dwellings import IWaterDwelling

class BettaFish(ISwimming, IWaterDwelling):

    def __init__(self, name):
        ISwimming.__init__(self)
        IWaterDwelling.__init__(self)
        self.name = name

    def __str__(self):
        return f'{self.name} the Betta Fish'
