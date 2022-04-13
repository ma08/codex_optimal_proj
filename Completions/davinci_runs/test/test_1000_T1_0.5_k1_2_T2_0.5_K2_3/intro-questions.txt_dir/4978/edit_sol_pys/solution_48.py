

def main():
    """
    This is the main function.
    """
    # Get the input
    input_str = input()
    input_str = input_str.split()
    rows = int(input_str[0])
    cols = int(input_str[1])

    grid = []
    for i in range(rows):
        input_str = input()
        grid.append(input_str)

    # This is the main loop
    while True:
        # This variable is used to determine if we should break out of the loop.
        done = True
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'V':
                    if i == 0:
                        done = False
                        if j > 0 and grid[i][j-1] == '.':
                            grid[i] = grid[i][:j-1] + 'V' + grid[i][j:]
                        if j < cols-1 and grid[i][j+1] == '.':
                            grid[i] = grid[i][:j+1] + 'V' + grid[i][j+2:]
                    else:
                        if grid[i-1][j] == '.':
                            done = False
                            grid[i-1] = grid[i-1][:j] + 'V' + grid[i-1][j+1:]
                        elif grid[i-1][j] == '#':
                            done = False
                            if j > 0 and grid[i][j-1] == '.':
                                grid[i] = grid[i][:j-1] + 'V' + grid[i][j:]
                            if j < cols-1 and grid[i][j+1] == '.':
                                grid[i] = grid[i][:j+1] + 'V' + grid[i][j+2:]

        if done:
            break

    # Print the grid
    for i in range(rows):
        print(grid[i])

if __name__ == "__main__":
    main()
