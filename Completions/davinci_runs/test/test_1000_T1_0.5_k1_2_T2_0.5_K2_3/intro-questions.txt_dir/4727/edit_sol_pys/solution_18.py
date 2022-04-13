

def merge(line, direction): 
    for i in range(3):
        if direction == "left":
            if line[i] == line[i+1]:
                line[i] = 2*line[i]
                line[i+1] = 0
        elif direction == "right":
            if line[i] == line[i+1]:
                line[i+1] = 2*line[i+1]
                line[i] = 0
    return line

def move(line, direction):
    if direction == "left":
        line = [x for x in line if x != 0]
        line = line + [0]*(4-len(line))
    elif direction == "right":
        line = [x for x in line if x != 0]
        line = [0]*(4-len(line)) + line
    return line

def main():
    grid = []
    for i in range(4):
        grid.append([int(x) for x in input().split()])
    direction = input()
    if direction == "0":
        for i in range(4):
            grid[i] = merge(grid[i], "left")
            grid[i] = move(grid[i], "left")
    elif direction == "1":
        for i in range(4):
            grid[i] = merge(grid[i], "up")
            grid[i] = move(grid[i], "up")
    elif direction == "2":
        for i in range(4):
            grid[i] = merge(grid[i], "right")
            grid[i] = move(grid[i], "right")
    elif direction == "3":
        for i in range(4):
            grid[i] = merge(grid[i], "down")
            grid[i] = move(grid[i], "down")
    for i in range(4):
        print(*grid[i])

if __name__ == "__main__":
    main()
