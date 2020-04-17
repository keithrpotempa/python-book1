class Aviary:
    instances = []
  
    def __init__(self):
        self.instances.append(self)
        self.animals = set()