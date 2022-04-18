

def main():
    """
    This is the main function.
    """
    # Get the input
    input_ = input().split()
    rows = int(input_[0]) # number of rows
    cols = int(input_[1]) # number of cols

    grid = [] # 2D array for the grid
    for i in range(rows):
        row = input() # get a row
        grid.append(row)

    # This is the main loop
    while True:
        # This variable is used to determine if we should break out of the loop
        done = True
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 'V':
                    if row == 0: # if on the top row
                        done = False # then we will make changes
                        if col > 0 and grid[row][col-1] == '.': # if there is a space to the left
                            grid[row] = grid[row][:col-1] + 'V' + grid[row][col:] # fill it with a V
                        if col < cols-1 and grid[row][col+1] == '.': # if there is a space to the right
                            grid[row] = grid[row][:col+1] + 'V' + grid[row][col+2:] # fill it with a V
                    else: # if on a row other than the top row
                        if grid[row-1][col] == '.': # if there is a space above
                            done = False # then we will make changes
                            grid[row-1] = grid[row-1][:col] + 'V' + grid[row-1][col+1:] # fill it with a V
                        elif grid[row-1][col] == '#': # if there is a # above
                            done = False # then we will make changes
                            if col > 0 and grid[row][col-1] == '.': # if there is a space to the left
                                grid[row] = grid[row][:col-1] + 'V' + grid[row][col:] # fill it with a V
                            if col < cols-1 and grid[row][col+1] == '.': # if there is a space to the right
                                grid[row] = grid[row][:col+1] + 'V' + grid[row][col+2:] # fill it with a V

        if done:
            break

    # Print the grid
    for row in range(rows):
        print(grid[row])

if __name__ == "__main__":
    main()
