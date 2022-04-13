

def main():
    grid = []
    for i in range(4):
        grid.append(list(map(int, input().split())))
    direction = int(input())
    if direction == 0:
        for j in range(4):
            for i in range(3):
                if grid[i][j] == 0:
                    for k in range(i+1, 4):
                        if grid[k][j] != 0:
                            grid[i][j] = grid[k][j]
                            grid[k][j] = 0
                            break
                if grid[i][j] != 0:
                    for k in range(i+1, 4):
                        if grid[k][j] != 0:
                            if grid[i][j] == grid[k][j]:
                                grid[i][j] *= 2
                                grid[k][j] = 0
                                break
    elif direction == 1:
        for j in range(4):
            for i in range(3):
                if grid[i][j] == 0:
                    for k in range(i+1, 4):
                        if grid[k][j] != 0:
                            grid[i][j] = grid[k][j]
                            grid[k][j] = 0
                            break
                if grid[i][j] != 0:
                    for k in range(i+1, 4):
                        if grid[k][j] != 0:
                            if grid[i][j] == grid[k][j]:
                                grid[i][j] *= 2
                                grid[k][j] = 0
                                break
    elif direction == 2:
        for j in range(4):
            for i in range(3, 0, -1):
                if grid[i][j] == 0:
                    for k in range(i-1, -1, -1):
                        if grid[k][j] != 0:
                            grid[i][j] = grid[k][j]
                            grid[k][j] = 0
                            break
                if grid[i][j] != 0:
                    for k in range(i-1, -1, -1):
                        if grid[k][j] != 0:
                            if grid[i][j] == grid[k][j]:
                                grid[i][j] *= 2
                                grid[k][j] = 0
                                break
    elif direction == 3:
        for j in range(4):
            for i in range(3, 0, -1):
                if grid[i][j] == 0:
                    for k in range(i-1, -1, -1):
                        if grid[j][k] != 0:
                            grid[j][i] = grid[j][k]
                            grid[j][k] = 0
                            break
                if grid[i][j] != 0:
                    for k in range(j-1, -1, -1):
                        if grid[k][i] != 0:
                            if grid[j][i] == grid[k][i]:
                                grid[j][i] *= 2
                                grid[k][i] = 0
                            break
    for i in range(4):
        for j in range(4):
            print(grid[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()
