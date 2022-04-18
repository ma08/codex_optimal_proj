

def main():
    grid = []
    for i in range(4):
        grid.append(list(map(int, input().split())))
    direction = int(input())
    if direction == 0:
        for i in range(4):
            for j in range(3):
                if grid[i][j] == 0:
                    for k in range(j+1, 4):
                        if grid[i][k] != 0:
                            grid[i][j], grid[i][k] = grid[i][k], 0
                            break
                if grid[i][j] != 0:
                    for k in range(j+1, 4):
                        if grid[i][k] != 0:
                            if grid[i][j] == grid[i][k]:
                                grid[i][j], grid[i][k] = grid[i][j]*2, 0
                            break                
    elif direction == 1:
        for i in range(4):
            for j in range(3):
                if grid[j][i] == 0:
                    for k in range(j+1, 4):
                        if grid[k][i] != 0:
                            grid[j][i], grid[k][i] = grid[k][i], 0
                            break
                if grid[j][i] != 0:
                    for k in range(j+1, 4):
                        if grid[k][i] != 0:
                            if grid[j][i] == grid[k][i]:
                                grid[j][i], grid[k][i] = grid[j][i]*2, 0
                            break
    elif direction == 2:
        for i in range(4):
            for j in range(3, 0, -1):
                if grid[i][j] == 0:
                    for k in range(j-1, -1, -1):
                        if grid[i][k] != 0:
                            grid[i][j], grid[i][k] = grid[i][k], 0
                            break
                if grid[i][j] != 0:
                    for k in range(j-1, -1, -1):
                        if grid[i][k] != 0:
                            if grid[i][j] == grid[i][k]:
                                grid[i][j], grid[i][k] = grid[i][j]*2, 0
                            break
    elif direction == 3:
        for i in range(4):
            for j in range(3, 0, -1):
                if grid[j][i] == 0:
                    for k in range(j-1, -1, -1):
                        if grid[k][i] != 0:
                            grid[j][i], grid[k][i] = grid[k][i], 0
                            break
                if grid[j][i] != 0:
                    for k in range(j-1, -1, -1):
                        if grid[k][i] != 0:
                            if grid[j][i] == grid[k][i]:
                                grid[j][i], grid[k][i] = grid[j][i]*2, 0
                            break
    for i in range(4):
        for j in range(4):
            print(grid[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()
