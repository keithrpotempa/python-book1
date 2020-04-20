from animals import Ant, BettaFish, CopperheadSnake, Earthworm, Finch, Gerbil, Mouse, PaintedDog, Parakeet, Penguin, Terrapin, TimberRattlesnake
from habitats import Aquarium
from containers import Aviary, Cage, FishBowl, Hutch

seaworld = Aquarium("Sea World")
aerie = Aviary()
big_cage = Cage()
big_bowl = FishBowl()
underground_thing = Hutch()

animal_classes = [Ant, BettaFish, CopperheadSnake, Earthworm, Finch, Gerbil, Mouse, PaintedDog, Parakeet, Penguin, Terrapin, TimberRattlesnake]
names = ["Liam", "Emma", "Noah", "Olivia", "William", "Ava", "James", "Isabella", "Oliver", "Sophia", "Benjamin", "Charlotte"]
containers = [Aviary, Cage, FishBowl, Hutch]

for animal_class in animal_classes:
    i = animal_classes.index(animal_class)
    name = names[i]
    name = animal_class(f"{name}")
    name.stow_away()

for container in containers:
    instance = container.instances[0]
    print(f"Animals in {instance}:")
    for animal in instance.animals:
        print(f"    - {animal}")

# for animal in seaworld.animals:
#     print(f'{animal} lives in Sea World')
