# In the previous Urban Planner exercise, you practices defining custom types to represent buildings. Now you need to create a type to represent your city. Here are the requirements for the class. You define the properties and methods.

# Name of the city.
# The mayor of the city.
# Year the city was established.
# A collection of all of the buildings in the city.
# A method to add a building to the city.
# Remember, each class should be in its own file. Define the City class in the city.py file.

class City:
  
  def __init__(self, name, mayor, year_established):
    self.name = name
    self.mayor = mayor
    self.year_established = year_established
    self.buildings = list()
  
  def add_building(self, building):
    self.buildings.append(building)