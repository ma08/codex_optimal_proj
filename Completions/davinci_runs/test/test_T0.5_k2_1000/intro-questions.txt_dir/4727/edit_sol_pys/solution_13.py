

def main():
    # read input
    grid = []
    for i in range(4):
        grid.append([int(x) for x in input().split()])
    direction = int(input())

    # move
    if direction == 0:
        # left
        for i in range(4):
            # remove zeros
            for j in range(4):
                if grid[i][j] == 0:
                    del grid[i][j]
                    grid[i].append(0)
            # merge
            for j in range(3):
                if grid[i][j] == grid[i][j+1]:
                    grid[i][j] *= 2
                    del grid[i][j+1]
                    grid[i].append(0)
    elif direction == 1:
        # up
        for i in range(4):
            # remove zeros
            for j in range(4):
                if grid[j][i] == 0:
                    del grid[j][i]
                    grid[j].insert(0, 0)
            # merge
            for j in range(3):
                if grid[j][i] == grid[j+1][i]:
                    grid[j][i] *= 2
                    del grid[j+1][i]
                    grid[j+1].insert(0, 0)
    elif direction == 2:
        # right
        for i in range(4):
            # remove zeros
            for j in range(4):
                if grid[i][3-j] == 0:
                    del grid[i][3-j]
                    grid[i].insert(0, 0)
            # merge
            for j in range(3):
                if grid[i][3-j] == grid[i][2-j]:
                    grid[i][3-j] *= 2
                    del grid[i][2-j]
                    grid[i].insert(0, 0)
    elif direction == 3:
        # down
        for i in range(4):
            # remove zeros
            for j in range(4):
                if grid[3-j][i] == 0:
                    del grid[3-j][i]
                    grid[3-j].insert(0, 0)
            # merge
            for j in range(3):
                if grid[3-j][i] == grid[2-j][i]:
                    grid[3-j][i] *= 2
                    del grid[2-j][i]
                    grid[2-j].insert(0, 0)
    else:
        print("Error: Direction not recognized.")

    # output
    for i in range(4):
        for j in range(4):
            print(grid[i][j], end=' ')
        print()

if __name__ == "__main__":
    main()
