class Aviary:
    instances = []
  
    def __init__(self):
        self.instances.append(self)
        self.animals = set()
        
    def __str__(self):
        return f'the Aviary'