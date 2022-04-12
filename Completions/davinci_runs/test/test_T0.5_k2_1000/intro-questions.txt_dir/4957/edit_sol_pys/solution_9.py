

def main():
    """
    This is the main function.
    """

    # Read in the first line.
    line = input()
    line = line.split(" ")
    n = int(line[0]) # number of rows
    m = int(line[1]) # number of columns

    # Read in the rest of the lines.
    grid = []
    for _ in range(n):
        line = input() # read in a row
        grid.append(list(line))

    # Go through each cell and determine whether or not it should be an espresso shop
    for row in range(n):
        for col in range(m):
            if grid[row][col] == '.': # if the cell is empty
                if row == 0:
                    if grid[row+1][col] == '.': # if the cell below is empty
                        grid[row][col] = 'E' # make it an espresso shop
                elif row == n-1:
                    if grid[row-1][col] == '.': # if the cell above is empty
                        grid[row][col] = 'E' # make it an espresso shop
                else:
                    if grid[row-1][col] == '.' or grid[row+1][col] == '.': # if the cell above or below is empty
                        grid[row][col] = 'E' # make it an espresso shop

                if col == 0:
                    if grid[row][col+1] == '.': # if the cell to the right is empty
                        grid[row][col] = 'E' # make it an espresso shop
                elif col == m-1:
                    if grid[row][col-1] == '.': # if the cell to the left is empty
                        grid[row][col] = 'E' # make it an espresso shop
                else:
                    if grid[row][col-1] == '.' or grid[row][col+1] == '.': # if the cell to the left or right is empty
                        grid[row][col] = 'E' # make it an espresso shop

    # Print out the grid.
    for row in range(n):
        for col in range(m):
            print(grid[row][col], end='') # print out the row
        print() # print a new line

main()
