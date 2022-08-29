def in_row(arr, row, number):
    for i in range(9):
        if(arr[row][i] == number):
            return True
    return False

def in_column(arr, col, number):
    for i in range(9):
        if(arr[i][col] == number):
            return True
    return False

def in_square(arr, row, col, number):
    for i in range(3):
        for j in range(3):
            if arr[row + i][col + j] == number:
                return True
    return False
def empty_locations(arr, location):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0: 
                location[0] = i
                location[1] = j
                return True
    return False

def solver(grid):
    location = [0,0]
    if empty_locations(grid, location) == False:
        return True
    else:
        row = location[0]
        col = location[1]
    # print(location)
    for i in range(1, 10):
        if(not in_row(grid, row, i) and not in_column(grid, col, i) and not in_square(grid, row - (row % 3), col - (col % 3), i)):
            # print("ye")
            grid[row][col] = i  
            if solver(grid):
                return True   
            grid[row][col] = 0
    return False

def print_board(grid):
    board = ""
    for i in range(9):
        board += "\n\n"
        for j in range(9):
            board += " " + str(grid[i][j]) + " "
    print(board)

if __name__ == "__main__":
    grid =[[0, 0, 0, 0, 0, 0, 6, 8, 0],
          [0, 0, 0, 0, 7, 3, 0, 0, 9],
          [3, 0, 9, 0, 0, 0, 0, 4, 5],
          [4, 9, 0, 0, 0, 0, 0, 0, 0],
          [8, 0, 3, 0, 5, 0, 9, 0, 2],
          [0, 0, 0, 0, 0, 0, 0, 3, 6],
          [9, 6, 0, 0, 0, 0, 3, 0, 8],
          [7, 0, 0, 6, 8, 0, 0, 0, 0],
          [0, 2, 8, 0, 0, 0, 0, 0, 0]]
    # print(in_row(grid, 0, 3))
    # print(empty_locations(grid))
    print_board(grid)
    # solver(grid)
    # print_board(grid)
    if solver(grid):
        print_board(grid)
    else:
        print("No Solution")
    
