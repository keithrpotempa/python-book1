from arrangements import Arrangement

# The Mother's Day arrangement contains daisies, baby's breath, and poppies. This arrangement is a bit more reserved, and Jake makes sure that each flower stem is cut to 4 inches.

# Also, each flower in this arrangement is organically grown with no pesticides used. Because of this, these arrangements have to be transported in a non-refrigerated container.

class MothersDay(Arrangement):
    instances = []

    def __init__(self, receiver):
        self.instances.append(self)
        self.holiday = "Mother's Day"
        super().__init__(self.holiday, receiver)