import random


class Insect:

    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.length_of_flight = 0

    def miles_flown(self):
        self.length_of_flight = random.randint(1, 10)
    
    def get_length_of_flight(self):
        return self.length_of_flight
        
