
import sys

def move(grid,direction):
    if direction == 0:
        for row in grid:
            i = 0
            while i < len(row):
                if row[i] == 0:
                    for j in range(i+1,len(row)):
                        if row[j] != 0:
                            row[i], row[j] = row[j], row[i]
                            break
                i += 1
            i = 0
            while i < len(row)-1:
                if row[i] == row[i+1]:
                    row[i] *= 2
                    del row[i+1]
                    row.append(0)
                    i += 1
                i += 1
        return grid
    elif direction == 1:
        grid_new = [[0]*4 for i in range(4)]
        for i in range(4):
            for j in range(4):
                grid_new[j][i] = grid[i][j]
        grid_new = move(grid_new,0)
        grid = [[0]*4 for i in range(4)]
        for i in range(4):
            for j in range(4):
                grid[i][j] = grid_new[j][i]
        return grid
    elif direction == 2:
        for row in grid:
            i = len(row)-1
            while i >= 0:
                if row[i] == 0:
                    for j in range(i-1,-1,-1):
                        if row[j] != 0:
                            row[i], row[j] = row[j], row[i]
                            break
                i -= 1
            i = len(row)-1
            while i > 0:
                if row[i] == row[i-1]:
                    row[i] *= 2
                    del row[i-1]
                    row.insert(0,0)
                    i -= 1
                i -= 1
        return grid
    elif direction == 3:
        grid_new = [[0]*4 for i in range(4)]
        for i in range(4):
            for j in range(4):
                grid_new[j][i] = grid[i][j]
        grid_new = move(grid_new,2)
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
        grid = move(grid,0)
    elif direction == 1:
        grid = move(grid,1)
    elif direction == 2:
        grid = move(grid,2)
    elif direction == 3:
        grid = move(grid,3)
    for row in grid:
        print(' '.join(map(str,row)))

if __name__ == '__main__':
    main()
