from vehicle import Vehicle

# [x] Define 5 of your favorite vehicles
# [x] Move all common properties in your vehicles to a new Vehicle class.
# [x] Create an instance of each vehicle.
# [x] Define a different value for each vehicle's properties.
# [x] Create a drive() method in the Vehicle class.
# [x] Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").
# [x] Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.
# [x] Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."
# [x] Make your vehicle instances perform all three behaviors.

# Vehicles
# Attak Trak

class AttakTrak(Vehicle):
  
    def __init__(self):
        name = "AttakTrak"
        maximum_occupancy = 4
        mobility_method = "tracks"
        super().__init__(name, maximum_occupancy, mobility_method)
        
    def drive(self):
        print(f"{self.name} uses its wildly rotating {self.mobility_method} to slowly move forward, carrying {self.maximum_occupancy}!")
        
    def turn(self, direction):
        print(f"The tracks on {self.name} rotate in opposite directions, making it turn to the {direction}")


# Wind Raider

class WindRaider(Vehicle):
  
    def __init__(self):
        name = "WindRaider"
        maximum_occupancy = 5
        mobility_method = "flight"
        super().__init__(name, maximum_occupancy, mobility_method)

    def drive(self):
        print(f"{self.name} uses its jet-propelled {self.mobility_method} to zip through the air, carrying {self.maximum_occupancy}!")

    def stop(self):
        print(f"{self.name} swoops down onto the ground and gracefully comes to a stop.")

        # defense = "lasers"
        
    def turn(self, direction):
        print(f"{self.name} zips to the {direction}.")
        
# # Battle Ram

class BattleRam(Vehicle):
  
    def __init__(self):
        name = "BattleRam"
        maximum_occupancy = 1
        mobility_method = "wheels"
        super().__init__(name, maximum_occupancy, mobility_method)
        
      # defense = "battering ram"
    #Detachable SkySled

# # Talon Fighter

class TalonFighter(Vehicle):
  
    def __init__(self):
        name = "TalonFighter"
        maximum_occupancy = 2
        mobility_method = "flight"
        super().__init__(name, maximum_occupancy, mobility_method)

    def stop(self):
        print(f"{self.name} performs an acrobatic feat in the sky before gracefully coming to perch on Point Dread.")
        
    def turn(self, direction):
        print(f"{self.name} zips to the {direction}.")

at = AttakTrak()
at.drive()
at.turn("left")
at.stop()
print()

wr = WindRaider()
wr.drive()
wr.turn("right")
wr.stop()
print()

br = BattleRam()
br.drive()
br.turn("left")
br.stop()
print()

tf = TalonFighter()
tf.drive()
tf.turn("right")
tf.stop()