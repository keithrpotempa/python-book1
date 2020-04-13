# Create an empty set named showroom.
showroom = set()

# Add four of your favorite car model names to the set.
showroom.update(["Car1", "Car2", "Car3", "Car4"])

# Print the length of your set.
print("Showroom length", len(showroom))

# Pick one of the items in your show room and add it to the set again.
showroom.update(["Car1"])

# Print your showroom. Notice how there's still only one instance of that model in there.
print(showroom)

# Using update(), add two more car models to your showroom with another set.
showroom.update({"Car5", "Car6"})
print(showroom)

# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("Car1")
print(showroom)

# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = set()

junkyard.update(["Car2", "Junk1", "Junk2", "Junk3"])

print(junkyard)

# Use the intersection method to see which cars exist in both the showroom and that junkyard.
print("Intersection", showroom.intersection(junkyard))

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
new_showroom = showroom.union(junkyard)

print(new_showroom)

# Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.
new_showroom.discard("Junk1")
print(new_showroom)