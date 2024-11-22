def is_valid_col(grid, col, val):
    for i in range(9):
        if grid[i][col] == val:
            return False
    return True
    
def is_valid_row(grid, row, val):
    for i in range(9):
        if grid[row][i] == val:
            return False
    return True
    
def is_vald_box(grid, row, col, val):
    for i in range(3):
        for j in range(3):
            if grid[i + (row - row%3)][j + (col - col%3)] == val:
                return False
    return True

# Returns True if val is a legal move on grid at: row,col
def is_valid_val(grid, row, col, val):
    return (is_valid_col(grid, col, val) and is_valid_row(grid, row, val) and is_vald_box(grid, row, col, val))

def find_empty_loc(grid, loc):
    for r in range(9):
        for c in range(9):
            if grid[r,c] == 0:
                loc[0] = r
                loc[1] = c
                return True
    return False

loc = [0,0] # stores the row and col indicies in the form: (ri,ci)
def solve_sudoku(grid):

    if find_empty_loc(grid, loc) == False:
        return True

    row = loc[0]
    col = loc[1]

    for i in range(1,10):

        if is_valid_val(grid, row, col, i) == True:

            grid[row,col] = i

            if solve_sudoku(grid) == True:
                return True
            
            grid[row,col] = 0
    
    return False
