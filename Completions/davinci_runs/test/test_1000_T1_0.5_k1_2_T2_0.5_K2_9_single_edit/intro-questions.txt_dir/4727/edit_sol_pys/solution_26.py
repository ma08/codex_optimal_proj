

def main():
    # Read input
    grid = []
    for i in range(4):
        grid.append([int(x) for x in input().split()])
    direction = int(input())

    # Move
    if direction == 0:
        # Left
        for i in range(4):
            # Remove zeros
            for j in range(4):
                if grid[i][j] == 0:
                    grid[i].pop(j)
                    grid[i].append(0)
            # Merge
            for j in range(3):
                if grid[i][j] == grid[i][j+1]:
                    grid[i][j] *= 2
                    grid[i].pop(j+1)
                    grid[i].append(0)
    elif direction == 1:
        # Up
        for i in range(4):
            # Remove zeros
            for j in range(4):
                if grid[j][i] == 0:
                    grid[j].pop(i)
                    grid[j].append(0)
            # Merge
            for j in range(3):
                if grid[j][i] == grid[j+1][i]:
                    grid[j][i] *= 2
                    grid[j+1].pop(i)
                    grid[j+1].append(0)
    elif direction == 2:
        # Right
        for i in range(4):
            # Remove zeros
            for j in range(4):
                if grid[i][3-j] == 0:
                    grid[i].pop(3-j)
                    grid[i].insert(0, 0)
            # Merge
            for j in range(3):
                if grid[i][3-j] == grid[i][2-j]:
                    grid[i][3-j] *= 2
                    grid[i].pop(2-j)
                    grid[i].insert(0, 0)
    elif direction == 3:
        # Down
        for i in range(4):
            # Remove zeros
            for j in range(4):
                if grid[3-j][i] == 0:
                    grid[3-j].pop(i)
                    grid[3-j].append(0)
            # Merge
            for j in range(3):
                if grid[3-j][i] == grid[2-j][i]:
                    grid[3-j][i] *= 2
                    grid[2-j].pop(i)
                    grid[2-j].append(0)
    else:
        print("Error: Direction not recognized.")

    # Output
    for i in range(4):
        for j in range(4):
            print(grid[i][j], end=' ')
        print()

if __name__ == "__main__":
    main()
