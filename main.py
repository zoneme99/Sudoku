import numpy as np
import random
from speed_calculator import calculate
import time
from itertools import permutations

class Grid:
    def __init__(self):
        self.grid = np.zeros((9,9), dtype=int)
        self.coord = self.create_coord()

    def print_grid(self):
        return print(self.grid)

    def create_coord(self):
        coord = []
        #middle grid
        for xgrid in range(3,6):
            for ygrid in range(3,6):
                coord.append([xgrid, ygrid])
        #side grid
        for xgrid in range(3,6):
            for ygrid in range(3):
                coord.append([xgrid, ygrid])
        #side grid
        for xgrid in range(3,6):
            for ygrid in range(6,9):
                coord.append([xgrid, ygrid])
        #side grid
        for xgrid in range(3):
            for ygrid in range(3,6):
                coord.append([xgrid, ygrid])
        #side grid
        for xgrid in range(6,9):
            for ygrid in range(3,6):
                coord.append([xgrid, ygrid])
        #corner grid
        for xgrid in range(3):
            for ygrid in range(3):
                coord.append([xgrid, ygrid])
        #corner grid
        for xgrid in range(6,9):
            for ygrid in range(3):
                coord.append([xgrid, ygrid])
        #corner grid
        for xgrid in range(3):
            for ygrid in range(6,9):
                coord.append([xgrid, ygrid])
        #corner grid
        for xgrid in range(6,9):
            for ygrid in range(6,9):
                coord.append([xgrid, ygrid])


        return coord

    def make_recursion_iterator(self):
        counter = [x for x in range(1, 10)]
        random.shuffle(counter)
        counter = iter(counter)
        return counter

    def test_axis(self, coord, iterator):
        xcoord = coord[0]
        ycoord = coord[1]
        for x in range(9):
            if self.grid[x][ycoord] == iterator:
                return False
        for y in range(9):
            if self.grid[xcoord][y] == iterator:
                return False
        return True
    
    def test_subgrid(self, coord, iterator):
        if (0 <= coord[0] <= 2) and (0 <= coord[1] <= 2):
            for x in range(3):
                for y in range(3):
                    if self.grid[x][y] == iterator:
                        return False
        
        if (3 <= coord[0] <= 5) and (0 <= coord[1] <= 2):
            for x in range(3,6):
                for y in range(3):
                    if self.grid[x][y] == iterator:
                        return False

        if (6 <= coord[0] <= 8) and (0 <= coord[1] <= 2):
            for x in range(6,9):
                for y in range(3):
                    if self.grid[x][y] == iterator:
                        return False
        
        if (0 <= coord[0] <= 2) and (3 <= coord[1] <= 5):
            for x in range(3):
                for y in range(3,6):
                    if self.grid[x][y] == iterator:
                        return False
        
        if (3 <= coord[0] <= 5) and (6 <= coord[1] <= 8):
            for x in range(3):
                for y in range(6,9):
                    if self.grid[x][y] == iterator:
                        return False
        
        if (3 <= coord[0] <= 5) and (3 <= coord[1] <= 5):
            for x in range(3,6):
                for y in range(3,6):
                    if self.grid[x][y] == iterator:
                        return False
        
        if (6 <= coord[0] <= 8) and (3 <= coord[1] <= 5):
            for x in range(6,9):
                for y in range(3,6):
                    if self.grid[x][y] == iterator:
                        return False
        
        if (3 <= coord[0] <= 5) and (6 <= coord[1] <= 8):
            for x in range(3,6):
                for y in range(6,9):
                    if self.grid[x][y] == iterator:
                        return False
        
        if (6 <= coord[0] <= 8) and (6 <= coord[1] <= 8):
            for x in range(6,9):
                for y in range(6,9):
                    if self.grid[x][y] == iterator:
                        return False
        return True
    
    def iterate(self, coord, index = 0):

        if index == 7:
            print("10%")
        elif index == 15:
            print("20%")
        elif index == 23:
            print("30%")    
        elif index == 31:
            print("40%")
        elif index == 39:
            print("50%")
        elif index == 47:
            print("60%")
        elif index == 55:
            print("70%")
        elif index == 63:
            print("80%")
        elif index == 71:
            print("90%")
        elif index == 80:
            print("100%")
        
        if index > len(coord)-1:
            return True
        iterator = self.make_recursion_iterator()
        
        try:
            while True:
                iternum = next(iterator)
                if self.test_axis(coord[index], iternum):
                    if self.test_subgrid(coord[index], iternum):
                        self.grid[coord[index][0]][coord[index][1]] = iternum
                        if self.iterate(coord, index+1):
                            return True
                        else:
                            self.grid[coord[index][0]][coord[index][1]] = 0
        except StopIteration:
            return False



    def fill_grid(self):
        if self.iterate(self.coord) == True:
            print("DONE")
            print(self.grid)

    def sudoku(self, empty_boxes):
        coord = random.shuffle(self.coord)
        numbers = []
        solutions = 1
        boxes = 0

        for x,y in coord:
            number = self.grid[x][y]
            self.grid[x][y] = 0
            boxes += 1
            numbers.append(number)
            combs = list(permutations(numbers))
            
            
            #if boxes == empty_boxes





            



# Exempel på hur man kan använda klasserna

# Skapa ett nytt grid
my_grid = Grid()

# Tilldela ett värde till en cell i en grids
#my_grid.grid[8][8] = 5

#print(my_grid.grid[my_grid.coord[0]])
#print(my_grid.coord[0][0])
#print(my_grid.test_subgrid([8,7], 5))
#my_grid.print_grid()
#print(calculate(my_grid.fill_grid)) 

#my_grid.fill_grid()
#my_grid.sudoku()

listing = list(permutations([1,2,3,4]))

for x in listing:
    print(x)