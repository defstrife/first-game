class Level:
    def __init__(self, name):
        self.name = name
        self.sublevels = {}

    def add_sublevel(self, direction, sublevel):
        self.sublevels[direction] = sublevel

    def get_sublevel(self, direction):
        return self.sublevels.get(direction)