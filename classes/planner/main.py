from building import Building
from city import City

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

# URBAN PLANNER II content:

# Create a new city instance and add your building instances to it. Once all buildings are in the city, iterate the city's building collection and output the information about each building in the city.

megalopolis = City("Megalopolis", "Mayor McCheese", 2001)

megalopolis.add_building(eight_hundred_eighth)
megalopolis.add_building(one_hundred_fiftieth)
megalopolis.add_building(oketo_hills)
megalopolis.add_building(oregon_trails_hq)
megalopolis.add_building(bingo_hall)

for building in megalopolis.buildings:
    print(f"{building.address} resides within {megalopolis.name}")