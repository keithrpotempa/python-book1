from movements import IWalking
from dwellings import IAboveGroundDwelling

class PaintedDog(IWalking, IAboveGroundDwelling):

    def __init__(self, name):
        IWalking.__init__(self)
        IAboveGroundDwelling.__init__(self)
        self.name = name

    def __str__(self):
        return f'{self.name} the Painted Dog'
