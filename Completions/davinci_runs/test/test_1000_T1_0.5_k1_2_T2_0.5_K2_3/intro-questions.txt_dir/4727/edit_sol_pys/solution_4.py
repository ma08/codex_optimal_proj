def merge(line, direction):
    if direction == "left":
        for i in range(4):
            for j in range(4):
                if j > 0 and line[j] == line[j-1]:
                    line[j-1] = 2*line[j-1]
                    line[j] = 0
    elif direction == "right":
        for i in range(4):
            for j in range(4):
                if j < 3 and line[j] == line[j+1]:
                    line[j+1] = 2*line[j+1]
                    line[j] = 0
    return line



def move(line, direction):
    if direction == "left":
        while 0 in line:
            line.remove(0)
        while len(line) < 4:
            line.append(0)
    elif direction == "right":
        while 0 in line:
            line.remove(0)
        while len(line) < 4:
            line.insert(0, 0)
    return line


def main():
    grid = []
    for i in range(4):
        grid.append([int(x) for x in input().split()])
    direction = input()
    for i in range(4):
        if direction == "0":
            grid[i] = merge(grid[i], "left")
            grid[i] = move(grid[i], "left")
        elif direction == "1":
            grid[i] = merge(grid[i], "right")
            grid[i] = move(grid[i], "right")
        elif direction == "2":
            grid[i] = merge(grid[i], "right")
            grid[i] = move(grid[i], "right")
        elif direction == "3":
            grid[i] = merge(grid[i], "right")
            grid[i] = move(grid[i], "right")
    for i in range(4):
        print(*grid[i])


if __name__ == "__main__":
    main()
