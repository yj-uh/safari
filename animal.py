class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 0

    def move(self, direction):
        print(f'moving to {direction}. <<< NOT IMPLEMENTED YET >>>')

    def breed(self, x, y):
        print(f'breed to {x}, {y}. <<< NOT IMPLEMENTED YET >>>')
        # return Animal(x, y)

class Zebra(Animal):
    def move(self, occupancy_grid):
        print('<<< NOT IMPLEMENTED >>>')
