

def main():
    """
    This is the main function.
    """

    # Read in the first line.
    line = raw_input()
    line = line.split()
    n = int(line[0])
    m = int(line[1])

    # Read in the rest of the lines.
    grid = []
    for _ in range(n):
        line = raw_input()
        grid.append(list(line))

    # Go through each cell and determine whether or not it should be a coffee shop.
    for row in range(n):
        for col in range(m):
            if grid[row][col] == '.':
                if row == 0:
                    if grid[row+1][col] == '.':
                        grid[row][col] = 'E'
                elif row == n-1:
                    if grid[row-1][col] == '.':
                        grid[row][col] = 'E'
                else:
                    if grid[row-1][col] == '.' or grid[row+1][col] == '.':
                        grid[row][col] = 'E'

                if col == 0:
                    if grid[row][col+1] == '.':
                        grid[row][col] = 'E'
                elif col == m-1:
                    if grid[row][col-1] == '.':
                        grid[row][col] = 'E'
                else:
                    if grid[row][col-1] == '.' or grid[row][col+1] == '.':
                        grid[row][col] = 'E'

    # Print out the grid.
    for row in range(n):
        for col in range(m):
            print(grid[row][col], end='')
        print()

main()
