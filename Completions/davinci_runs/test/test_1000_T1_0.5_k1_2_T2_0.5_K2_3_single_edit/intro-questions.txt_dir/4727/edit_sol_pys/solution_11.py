

def merge(grid, direction):
    if direction == "left":
        for i in range(4):
            for j in range(4):
                if j > 0 and grid[i][j] == grid[i][j-1]:
                    grid[i][j-1] = 2*grid[i][j-1]
                    grid[i][j] = 0
    elif direction == "right":
        for i in range(4):
            for j in range(4):
                if j < 3 and grid[i][j] == grid[i][j+1]:
                    grid[i][j+1] = 2*grid[i][j+1]
                    grid[i][j] = 0
    return grid

def move(grid, direction):
    if direction == "left":
        for i in range(4):
            while 0 in grid[i]:
                grid[i].remove(0)
            while len(grid[i]) < 4:
                grid[i].append(0)
    elif direction == "right":
        for i in range(4):
            while 0 in grid[i]:
                grid[i].remove(0)
            while len(grid[i]) < 4:
                grid[i].insert(0, 0)
    return grid

def main():
    grid = []
    for i in range(4):
        grid.append([int(x) for x in input().split()])
    direction = input()
    for i in range(4):
        if direction == "0":
            grid = merge(grid, "up")
            grid = move(grid, "up")
        elif direction == "1":
            grid = merge(grid, "down")
            grid = move(grid, "down")
        elif direction == "2":
            grid = merge(grid, "right")
            grid = move(grid, "right")
        elif direction == "3":
            grid = merge(grid, "left")
            grid = move(grid, "left")
    for i in range(4):
        print(*grid[i])

if __name__ == "__main__":
    main()
