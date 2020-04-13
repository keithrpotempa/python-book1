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

# Once defined this way, you can send those values as parameters when you create each instance

eight_hundred_eighth = Building("800 8th Street", 12)

# Creating Your Buildings
# Create 5 building instances

one_hundred_fiftieth = Building("100 50th Street", 29)
oketo_hills = Building("1 Oketo Street", 15)
oregon_trails_hq = Building("1 Oregon Trails", 5)
bingo_hall = Building("North North Street", 1)

# Have each one get purchased by a real estate magnate

eight_hundred_eighth.purchase("Lawson, Inc.")
one_hundred_fiftieth.purchase("Magnolia Estate Magnate")
oketo_hills.purchase("Dario Argento, Inc.")
oregon_trails_hq.purchase("Sierra, LLC.")
bingo_hall.purchase("Field Hill Assisted Living")

# After purchased, construct each one
eight_hundred_eighth.construct()
one_hundred_fiftieth.construct()
oketo_hills.construct()
oregon_trails_hq.construct()
bingo_hall.construct()

# Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.
# Example
# 800 8th Street was purchased by Bob Builder on 03/14/2018 and has 12 stories.

eight_hundred_eighth.output()
one_hundred_fiftieth.output()
oketo_hills.output()
oregon_trails_hq.output()
bingo_hall.output()
