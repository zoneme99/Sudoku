import numpy as np
import random
import time
from itertools import permutations, chain
import sys
sys.setrecursionlimit(10000)

class Grid:
    def __init__(self, comment=False):
        self.grid = np.zeros((9,9), dtype=int)
        self.coord = self.create_coord()
        self.comment = comment

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

        if self.comment == True:
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

    def sudoku(self, empty_boxes):  #Tar bort antalet rutor till angivet antal, undviker dubbla lösningar
        coord = self.coord
        random.shuffle(coord)
        numbers = []
        emptycoord = []
        self.boxes = 0
        self.multisolutions = False

        for x,y in coord:
            print("test")
            errors = []
            if self.boxes == empty_boxes:
                break
            numbers.append(self.grid[x][y])
            emptycoord.append([x,y])
            self.grid[x][y] = 0
            self.boxes += 1


  
            self.filter_newcombs(errors, emptycoord, numbers)

        print("Grattis ett färdigt Sudoku")
        return self.print_grid()
    
    def filter_newcombs(self, errors, emptycoord, numbers):

                    combsraw = permutations(numbers)
                    combs = filter(lambda x: x != tuple(numbers), combsraw) #tar bort första lösningen
                    tic = time.perf_counter()
                    filtered_combs = self.filter_comb(combs, emptycoord, errors) #filterar bort all onödiga kombinationer
                    print("filter time")
                    print(time.perf_counter() - tic)
                    tic = time.perf_counter() 
                    self.test_combs(filtered_combs, emptycoord) #testar kombinationerna
                    print("test time")
                    print(time.perf_counter() - tic)
                    if self.multisolutions:
                        for x, y in emptycoord:
                            self.grid[x][y] = 0
                        self.grid[x][y] = numbers[-1]
                        emptycoord.pop()
                        numbers.pop()
                        self.boxes -= 1
                        return None


    def filter_comb(self, combs, emptycoord, errors):
        for i in range(len(emptycoord)): #Testar möjliga kombinationer 
            for perms in combs:
                for number in perms:
                    if not (self.test_subgrid(emptycoord[i], number) and self.test_axis(emptycoord[i], number)):
                        errors.append([i, number])
                        filtered_combs = (perm for perm in combs if all(perm[pos] != number for pos, number in errors)) #SEEEEEEEEEEEEEEEEEEEEEEEEEEEE ATTTTTTTTTTTTTTTTTTT DEN FUNKAR
                        return self.filter_comb(filtered_combs, emptycoord, errors)
        return combs


                

    def test_combs(self, filtered_combs, emptycoord):
        for comb in filtered_combs: #Testar möjliga kombinationer
            for i, number in enumerate(comb):
                if self.test_subgrid(emptycoord[i], number) and self.test_axis(emptycoord[i], number): # KOMMER ALDRIG IN
                    self.grid[emptycoord[i][0]][emptycoord[i][1]] = number
                    print("INSERT")
                    if i == len(comb) - 1:
                        print("Warning, double solutions")
                        print("{}e boxen krascha det!".format(self.boxes))
                        self.multisolutions = not self.multisolutions
                else:
                    for x, y in emptycoord:
                        self.grid[x][y] = 0
                    break
            if self.multisolutions:
                break
        



my_grid = Grid()

my_grid.fill_grid()
my_grid.sudoku(8)

