# Create a tuple named zoo that contains 10 of your favorite animals.
zoo = ("Kangaroo", "Aardwolf", "Alpaca", "Alligator", "Bison", "Cat", "Cheetah", "Chuckwalla", "Flamingo", "Crow")

# Find one of your animals using the tuple.index(value) syntax on the tuple.
# # Example
# flowers = ("daisy", "rose")
# flower.index("rose") # Output is 1

print(zoo.index("Flamingo"))


# Determine if an animal is in your tuple by using value in tuple syntax.
# animal_to_find = "kangaroo"
# if animal_to_find in zoo:
#     # Print that the animal was found

animal_to_find = "Flamingo"
if animal_to_find in zoo:
  print(f"Zoo contains a {animal_to_find}")

# You can reverse engineer (unpack) a tuple into another tuple with the following syntax.
# children = ("Sally", "Hansel", "Gretel", "Svetlana")
# (first_child, second_child, third_child, fourth_child) = children
# print(first_child) # Output is "Sally"
# print(second_child) # Output is "Hansel"
# print(third_child) # Output is "Gretel"
# print(fourth_child) # Output is "Svetlana"

# Create a variable for the animals in your zoo tuple, and print them to the console.
# Convert your tuple into a list.

animals = list(zoo)


# Use extend() to add three more animals to your zoo.

animals.extend(["Dinosaur", "Bicycle", "Rodent"])

print(animals)
# Convert the list back into a tuple.

print(tuple(animals))