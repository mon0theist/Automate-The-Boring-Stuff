# ATBS Chapter 4 - Character Picture Grid
#
# 3rd attempt for review/revision purposes
#
# No looking at previous attempts or solutions!
#
# Hint: You will need to use a loop in a loop in order to print grid[0][0], then grid[1][0], then grid[2][0], and so on, up to grid[8][0]. This will finish the first row, so then print a newline. Then your program should print grid[0][1], then grid[1][1], then grid[2][1], and so on. The last thing your program will print is grid[8][5].

# Also, remember to pass the end keyword argument to print() if you don’t want a newline printed automatically after each print() call.

# y = which list (inner/nested loop)
# x = which value in list y (outer loop, only changes after inner loop finishes)
# grid[y][x]

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(len(grid[0])): # could be len() of grid[0-9], they're all the same len
# either way it's going to iterate 6 times, so 0-5
    for j in range(len(grid)): # going down the grid, so 9
        print(grid[j][i], end='')
    print('\n') # every outer loop iteration should be on it's own line

# had to look at a previous attempt/solution because I can't quite grasp nested loops
# but I think I was able to understand and follow this time. Just makes my brain hurt
