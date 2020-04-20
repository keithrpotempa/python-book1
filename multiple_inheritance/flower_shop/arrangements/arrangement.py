class Arrangement:

    def __init__(self, holiday, receiver):
        self.receiver = receiver
        self.holiday = holiday
        self.flowers = []

    def enhance(self, flower):
        self.flowers.append(flower)
        print(f"{flower.name} added to {self.holiday} Arrangement for {self.receiver}")
        
    def describe(self):
        if len(self.flowers) == 0:
            print(f"Arrangement for {self.holiday} is empty.")
        elif self.holiday:
            print(f"Arrangement is for {self.receiver} for {self.holiday} and contains the following flowers:")
            for flower in self.flowers:
                if flower.color:
                    print(f"    - {flower.name} ({flower.color})")
                else:
                    print(f"    - {flower.name}")