
def main():
    """
    This is the main function.
    """

    # Read in the first line.
    line = input()
    line = line.split()
    n = int(line[0])
    m = int(line[1])

    # Read in the rest of the lines.
    grid = []
    for _ in range(n):
        line = input()
        grid.append(list(line))

    # Go through each cell and determine whether or not it should be a coffee shop.
    for row in range(n):
        for col in range(m):
            if grid[row][col] == '.':
                if ((row == 0 and grid[row+1][col] == '.') or
                    (row == n-1 and grid[row-1][col] == '.') or
                    (col == 0 and grid[row][col+1] == '.') or
                    (col == m-1 and grid[row][col-1] == '.') or
                    (row-1 >= 0 and grid[row-1][col] == '.') or
                    (row+1 < n and grid[row+1][col] == '.') or
                    (col-1 >= 0 and grid[row][col-1] == '.') or
                    (col+1 < m and grid[row][col+1] == '.')):
                        grid[row][col] = 'E' 

    # Print out the grid.
    for row in range(n):
        for col in range(m):
            print(grid[row][col], end='')
        print()

main()
