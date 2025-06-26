import random

class Card:
    def __init__(self, value)
        self.value = value
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def __str__(self):
        if self.is_open:
            return str(self.value)
        else:
            return "*"

class Game:
    def __init__(self):
        self.fiels = []
        values = [1,2,3,4,5,6,7,8]
        random.shuffle(values)
        for v in values:
