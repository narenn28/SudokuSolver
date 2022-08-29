### sudoku board generator

## must leave at least 17 values in board in order to have only one solution
from SudokuSolver import *
import random

def safe_location(grid, row, col, value):
    if ((not in_row(grid, row, value)) and (not in_column(grid, col, value)) and (not in_square(grid, row - (row % 3), col - (col % 3), value))):
        return True
    return False

# def value_picker(grid, row, col):
#     value = random.randint(1,9)
#     if(not safe_location(grid, row, col, value)):
#         value_picker(grid, row, col)
#     return value

value_list = [1,2,3,4,5,6,7,8]
# def grid_generator(grid):
#     if empty_locations(grid, [0,0]) == False:
#         return True
#     for i in range(81):
#         row = i // 9
#         col = i % 9
#         if grid[row][col] == 0:
#             random.shuffle(value_list)
#             for val in value_list:
#                 if val not in grid[row]:
#                     if not in_column(grid, col, val):
#                         if not in_square(grid, row - (row % 3), col - (col % 3), val):
#                             grid[row][col] = val
#                             # if empty_locations(grid, [0,0]) == False:
#                             #     return True
#                             # else:
#                             if grid_generator(grid):
#                                 return True
#                             grid[row][col] = 0          
#     return False
                            
def fillGrid(grid):
    global counter
    #Find next empty cell
    for i in range(0,81):
        row=i//9
        col=i%9
        if grid[row][col]==0:
            random.shuffle(value_list)      
            for value in value_list:
                #Check that this value has not already be used on this row
                if not(value in grid[row]):
                    #Check that this value has not already be used on this column
                    if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
                        #Identify which of the 9 squares we are working on
                        square=[]
                        if row<3:
                            if col<3:
                                square=[grid[i][0:3] for i in range(0,3)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(0,3)]
                            else:  
                                square=[grid[i][6:9] for i in range(0,3)]
                        elif row<6:
                            if col<3:
                                square=[grid[i][0:3] for i in range(3,6)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(3,6)]
                            else:  
                                square=[grid[i][6:9] for i in range(3,6)]
                        else:
                            if col<3:
                                square=[grid[i][0:3] for i in range(6,9)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(6,9)]
                            else:  
                                square=[grid[i][6:9] for i in range(6,9)]
                        #Check that this value has not already be used on this 3x3 square
                        if not value in (square[0] + square[1] + square[2]):
                            grid[row][col]=value
                            if not empty_locations(grid, [0,0]):
                                return True
                            else:
                                if fillGrid(grid):
                                    return True
            break
    grid[row][col]=0     

base  = 3
side  = base*base

# pattern for a baseline valid solution
def pattern(r,c): return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)
from random import sample
def shuffle(s): return sample(s,len(s)) 
rBase = range(base) 
rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
nums  = shuffle(range(1,base*base+1))

# produce board using randomized baseline pattern
board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

for line in board: print(line)
            
            

if __name__ == "__main__":
    grid =[[0 for x in range(9)]for y in range(9)]
    print_board(grid)
    fillGrid(grid)
    print_board(grid)

    
