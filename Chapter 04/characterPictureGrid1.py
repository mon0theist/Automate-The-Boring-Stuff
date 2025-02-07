# Character Picture Grid
#
# Say you have a list of lists where each value in the inner lists is a one-character string, like this:
#
#
# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]
#
# You can think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters. The (0, 0) origin will be in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase going down.

# >>> spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
# >>> spam[0]
# ['cat', 'bat']
# >>> spam[0][1]
# 'bat'
# >>> spam[1][4]
# 50

# The first index dictates which list value to use, and the second indicates the value within the list value. For example, spam[0][1] prints 'bat', the second value in the first list. If you only use one index, the program will print the full list value at that index.

# based on this it seems that in grid[y][x] is more accurate...

# Copy the previous grid value, and write code that uses it to print the image.
#
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....

# This is the above image sideways

# Hint: You will need to use a loop in a loop in order to print grid[0][0], then grid[1][0], then grid[2][0], and so on, up to grid[8][0]. This will finish the first row, so then print a newline. Then your program should print grid[0][1], then grid[1][1], then grid[2][1], and so on. The last thing your program will print is grid[8][5].

# Also, remember to pass the end keyword argument to print() if you don’t want a newline printed automatically after each print() call.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for j in range(len(grid[0])): # this is basically functioning as the Y axis?
    for i in range(0, len(grid)): # this is basically functioning as the X axis?
        print(grid[i][j], end='') # keyword=end prevents a newline after every print()
    print()

# I don't follow this at all.... :'(
