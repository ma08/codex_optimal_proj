import sys

def move_left(grid):
    for row in grid:
        for i in range(len(row)):
            if row[i] == 0:
                for j in range(i+1,len(row)):
                    if row[j] != 0:
                        row[i], row[j] = row[j], row[i]
                        break
        for i in range(len(row)-1):
            if row[i] == row[i+1]:
                row[i] *= 2
                del row[i+1]
                row.append(0)
                i += 1
    return grid

def move_up(grid):
    grid_new = [[0]*4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            grid_new[j][i] = grid[i][j]
    grid_new = move_left(grid_new)
    grid = [[0]*4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            grid[i][j] = grid_new[j][i]
    return grid

def move_right(grid):
    for row in grid:
        for i in range(len(row)-1,-1,-1):
            if row[i] == 0:
                for j in range(i-1,-1,-1):
                    if row[j] != 0:
                        row[i], row[j] = row[j], row[i]
                        break
        for i in range(len(row)-1,0,-1):
            if row[i] == row[i-1]:
                row[i] *= 2
                del row[i-1]
                row.insert(0,0)
                i -= 1
    return grid

def move_down(grid):
    grid_new = [[0]*4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            grid_new[j][i] = grid[i][j]
    grid_new = move_right(grid_new)
    grid = [[0]*4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            grid[i][j] = grid_new[j][i]
    return grid

def main():
    grid = []
    for i in range(4):
        grid.append(list(map(int,sys.stdin.readline().strip().split())))
    direction = int(sys.stdin.readline().strip())
    if direction == 0:
        grid = move_left(grid)
    elif direction == 1:
        grid = move_up(grid)
    elif direction == 2:
        grid = move_right(grid)
    elif direction == 3:
        grid = move_down(grid)
    for row in grid:
        print(' '.join(map(str,row)))

if __name__ == '__main__':
    main()
