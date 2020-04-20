from movements import IDigging, IWalking
from dwellings import IAboveGroundDwelling

class Mouse(IDigging, IWalking, IAboveGroundDwelling):

    def __init__(self, name):
        IDigging.__init__(self)
        IWalking.__init__(self)
        IAboveGroundDwelling.__init__(self)
        self.name = name

    def __str__(self):
        return f'{self.name} the Mouse'
