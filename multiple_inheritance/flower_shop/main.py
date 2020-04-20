import random
from flowers import Alstroemeria, BabysBreath, Daisy, Lily, Poppy, Rose
from arrangements import ValentinesDay, MothersDay

if __name__ == "__main__":
    flower_classes = [Alstroemeria, BabysBreath, Daisy, Lily, Poppy, Rose]
    names = ["Liam", "Emma", "Noah", "Olivia", "William", "Ava", "James", "Isabella", "Oliver", "Sophia", "Benjamin", "Charlotte"]
    colors = ["Red", "Pink", "Blue"]
    arrangement_classes = [ValentinesDay, MothersDay]

    # Loop through a list of arbitrary names
    for name in names:
        #Create an arrangement (randomly choose one holiday)
        arrangement_class = random.choice(arrangement_classes)
        arrangement = arrangement_class(f"{name}")
        #For that arrangement, loop through every flower class
        for flower_class in flower_classes:
            i = flower_classes.index(flower_class)
            color = random.choice(colors)
            #Make a flower of a random color
            flower = flower_class(f"{color}")
            #Add it to the present arrangement
            arrangement.enhance(flower)       
        #Once both loops have finished,
        #Print out the summary of the arrangement
        arrangement.describe()
  