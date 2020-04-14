from datetime import datetime

# Properties
# designer - It will hold your name.
# date_constructed - This will hold the exact time the building was created.
# owner - This will store the same of the person who owns the building.
# address
# stories

class Building:

# Constructor
# Define your __init__ method to accept two arguments
# address
# stories
  
    def __init__(self, address, stories):
        self.designer = "Keith"
        self.date_constructed = "TBD"
        self.owner = "TBD"
        self.address = address
        self.stories = stories
        

# Methods
# Define a construct() method. The method's logic should set the date_constructed field's value to datetime.datetime.now(). You will need to have import datetime at the top of your file.

    def construct(self):
        self.date_constructed = datetime.now()


# Define a purchase() method. The method should accept a single string argument of the name of the person purchasing a building. The method should take that string and assign it to the owner property.

    def purchase(self, purchaser_name):
        self.owner = purchaser_name


    def output(self):
      print(f"{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.")