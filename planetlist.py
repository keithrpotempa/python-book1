planet_list = ["Mercury", "Mars"]

# Use append() to add Jupiter and Saturn at the end of the list.

planet_list.append("Jupiter")
planet_list.append("Saturn")

# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.

# planet_list.extend(["Earth", "Neptune", "Venus"])

# Use insert() to add Earth, and Venus in the correct order.

planet_list.insert(0, "Earth")
planet_list.insert(-1, "Venus")

# Use append() again to add Pluto to the end of the list.

planet_list.append("Pluto")

# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.

rocky_planets = planet_list[0:3]
rocky_planets.append(planet_list[4])

# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.

del planet_list[-1]

print("planets", planet_list)
print("rocky planets", rocky_planets)

# Challenge: Iterating over planets
# Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on.

# Example spacecraft list
spacecraft = [
    ("Pioneer 10", ["Jupiter"]),
    ("Pioneer 11", ["Jupiter", "Saturn"]),
    ("Voyager 1", ["Jupiter", "Saturn"]),
    ("Gallileo", ["Jupiter"]),
    ("Ulysses", ["Jupiter"]),
    ("New Horizons", ["Jupiter"]),
    ("Juno", ["Jupiter"]),
    ("Voyager 2", ["Uranus", "Neptune", "Saturn", "Uranus"]),
    ("Cassini", ["Jupiter", "Saturn"]),
    ("Huygens", ["Saturn"]),
    ("Viking", "Mars")
]

# Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited it.

for planet in planet_list:
    satellites_visited = []
    for craft,planets_visited in spacecraft:
      if planet in planets_visited:
        satellites_visited.append(craft)
    if len(satellites_visited) == 0:
      print(f"no satellites have visited {planet}")
    if len(satellites_visited) > 1:
      print(f"{satellites_visited} have visited {planet}")
    if len(satellites_visited) == 1:
      print(f"{satellites_visited} has visited {planet}")
    