
def main():
    """
    This is the main function.
    """

    # Read in the first line and split it into two numbers.
    n, m = input().split()
    n = int(n)
    m = int(m)

    # Read in the rest of the lines and store them in a 2D array.
    grid = []
    for _ in range(n):
        line = input()
        grid.append(list(line))

    # Go through each cell and determine whether or not it should be a restaurant.
    for row in range(n):
        for col in range(m):
            if grid[row][col] == '.':
                # Check the cell above.
                if row == 0 or grid[row-1][col] == '.':
                    # Check the cell below.
                    if row == n-1 or grid[row+1][col] == '.':
                        # Check the cell to the left.
                        if col == 0 or grid[row][col-1] == '.':
                            # Check the cell to the right.
                            if col == m-1 or grid[row][col+1] == '.':
                                grid[row][col] = 'E'

    # Print out the grid.
        print(''.join(grid[row]))

main()
