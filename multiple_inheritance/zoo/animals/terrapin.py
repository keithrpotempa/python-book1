from movements import IDigging, ISwimming, IWalking
from dwellings import IAboveGroundDwelling

class Terrapin(IDigging, ISwimming, IWalking, IAboveGroundDwelling):

    def __init__(self, name):
        IDigging.__init__(self)
        ISwimming.__init__(self)
        IWalking.__init__(self)
        IAboveGroundDwelling.__init__(self)
        self.name = name

    def __str__(self):
        return f'{self.name} the Terrapin'
