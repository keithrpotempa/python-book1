class Vehicle:
  
    def __init__(self, name, maximum_occupancy, mobility_method):
        self.name = name
        self.maximum_occupancy = maximum_occupancy
        self.mobility_method = mobility_method
        
    def describe(self):
        print(f"{self.name} uses {self.mobility_method} to move and can seat {self.maximum_occupancy}." )
        
    def drive(self):
        print(f"{self.name} zooms off with {self.mobility_method} carrying {self.maximum_occupancy}!")
        
    def turn(self, direction):
        print(f"{self.name} turns to the {direction}.")
        
    def stop(self):
        print(f"{self.name} grinds to a halt.")