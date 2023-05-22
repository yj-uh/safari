import os 
import random
from animal import Empty, Zebra, Lion
from utils import print_TODO

class CircleOfLife:
    def __init__(self, world_size, num_zebras, num_lions):
        self.world_size = world_size
        self.grid = [[Empty(y, x) for y in range(self.world_size)]
                                  for x in range(self.world_size)]
        zebra_coords, lion_coords = self.get_random_coords(num_zebras, num_lions)
        for y, x in zebra_coords:
            self.grid[y][x] = Zebra(y, x) 
        for y, x in lion_coords:
            self.grid[y][x] = Lion(y, x)
        self.timestep = 0
        print('Welcome to AIE Safari!')
        print(f'\tworld size = {world_size}')
        print(f'\tnumber of zebras = {num_zebras}')
        print(f'\tnumber of lions = {num_lions}')

    def get_random_coords(self, num_zebras, num_lions):
        all_coords = [(y, x) for y in range(self.world_size)
                       for x in range(self.world_size)]
        zebra_coords = random.sample(all_coords, num_zebras)
        all_coords = list(set(all_coords) - set(zebra_coords))
        lion_coords = random.sample(all_coords, num_lions)
        return zebra_coords, lion_coords

    def display(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print(f'Clock: {self.timestep}')
        top_coord_str = ' '.join([f'{coord}' for coord in range(len(self.grid))])
        print('   ' + top_coord_str)
        for row, line in enumerate(self.grid):
            buffer = [str(animal) for animal in line]
            print(f'{row:2} ' + ' '.join(buffer))
        key = input('enter [q] to quit:')
        if key == 'q':
            exit()

    def step_move(self):
        animals = [animal for line in self.grid for animal in line
                   if not isinstance(animal, Empty)]
        for animal in animals:
            if animal.hp != 0:
                animal.move(self.grid)

    def step_breed(self):
        animals = [animal for line in self.grid for animal in line
                   if not isinstance(animal, Empty)
                   and animal.is_ready_to_breed()]
        for animal in animals:
            animal.breed(self.grid)

    def housekeeping(self):
        for y, line in enumerate(self.grid):
            for x, animal in enumerate(line):
                if animal.hp == 0:
                    self.grid[y][x] = Empty(y, x)
                else:
                    self.grid[y][x].age += 1

    def run(self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep += 1
            self.step_move()
            self.display()
            self.step_breed()
            self.display()
            self.housekeeping()


if __name__ == '__main__':
    safari = CircleOfLife(5, 5, 2)
    # safari.display()
    # safari.step_move()
    # safari.step_breed()
    safari.run(10)