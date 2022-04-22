
def stars(n,m,grid):
    k = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                k += 1
                grid[i][j] = '.'
                s = 1
                    if grid[i + s][j] == '*' and grid[i - s][j] == '*' and grid[i][j + s] == '*' and grid[i][j - s] == '*':
                        grid[i + s][j] = '.'
                        grid[i - s][j] = '.'
                        grid[i][j + s] = '.'
                        grid[i][j - s] = '.'
                        s += 1
                    else:
                        break
                print(i + 1, j + 1, s - 1)
    if k == 0:
        print(-1)



n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(input()))
stars(n, m, grid)
