from arrangements import Arrangement

# The Valentine's Day arrangement includes the traditional rose. Jake has red, pink, and blue ones to send the right message. It also has lillies and alstroemeria to add more depth to the color of the arrangement.

# This arrangment is flamboyant and extravagent. Each flower stem is cut to 7 inches. Flowers in this arrangement are not organically grown, so they can be transported in a refrigerated container.

class ValentinesDay(Arrangement):
    instances = []
    
    def __init__(self, receiver):
        self.instances.append(self)
        self.holiday = "Valentine's Day"
        super().__init__(self.holiday, receiver)
        
    # Override the `enhance` method to ensure only
    # roses, lillies, and alstroemeria can be added
    def enhance(self, flower):
        # self.flowers.append(flower)
        if flower.name == "Rose" or flower.name == "Lily" or flower.name == "Alstroemeria":
            self.flowers.append(flower)
            print(f"{flower.name} added to {self.holiday} Arrangement for {self.receiver}")
        else:
            pass