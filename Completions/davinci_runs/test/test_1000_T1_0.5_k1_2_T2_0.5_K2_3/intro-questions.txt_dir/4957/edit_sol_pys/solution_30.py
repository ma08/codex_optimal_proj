
def main():
    """
    This is the main function.
    """

    # Read in the first line and split it.
    line = input().split()
    n = int(line[0]) # number of rows
    m = int(line[1]) # number of columns

    # Read in the rest of the lines and create a grid.
    grid = []
    for _ in range(n):
        line = input()
        grid.append(list(line))

    # Go through each cell and determine whether or not it should be a coffee shop.
    for row in range(n):
        for col in range(m):
            if grid[row][col] == '.':
                if (row == 0 and grid[row+1][col] == '.') or \
                    (row == n-1 and grid[row-1][col] == '.') or \
                    (col == 0 and grid[row][col+1] == '.') or \
                    (col == m-1 and grid[row][col-1] == '.') or \
                    (row != 0 and row != n-1 and (grid[row-1][col] == '.' or grid[row+1][col] == '.')) or \
                    (col != 0 and col != m-1 and (grid[row][col-1] == '.' or grid[row][col+1] == '.')):
                    grid[row][col] = 'E'

    # Print out the grid.
    for row in range(n):
        for col in range(m):
            print(grid[row][col], end='')
        print()

main()
