from arrangements import Arrangement

# The Valentine's Day arrangement includes the traditional rose. Jake has red, pink, and blue ones to send the right message. It also has lillies and alstroemeria to add more depth to the color of the arrangement.

# This arrangment is flamboyant and extravagent. Each flower stem is cut to 7 inches. Flowers in this arrangement are not organically grown, so they can be transported in a refrigerated container.

class ValentinesDay(Arrangement):
  
    def __init__(self):
        holiday = "Valentine's Day"
        super().__init__(holiday)
        
    # Override the `enhance` method to ensure only
    # roses, lillies, and alstroemeria can be added
    def enhance(self, flower):
        # self.flowers.append(flower)
        if flower.name == "Rose" or flower.name == "Lilly" or flower.name == "Alstroemeria":
            self.flowers.append(flower)
        else:
            print(f"Only roses, lillies, and alstroemeria can be added to a {self.holiday} Arrangement.")