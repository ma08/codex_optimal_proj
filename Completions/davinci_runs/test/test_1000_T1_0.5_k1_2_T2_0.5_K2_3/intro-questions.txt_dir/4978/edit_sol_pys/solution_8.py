

def main():

    # Get the input
    input_ = input()
    input_ = input_.split()
    rows = int(input_[0])
    cols = int(input_[1])

    grid = []
    for i in range(rows):
        row = input()
        grid.append(row)


    while True:

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
