

def stars(n,m,grid):
    # print(grid)
    k = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                k += 1
                grid[i][j] = '.'
                s = 1
                while i+s < n and i-s >= 0 and j+s < m and j-s >= 0:
                    if grid[i+s][j] == '*' and grid[i-s][j] == '*' and grid[i][j+s] == '*' and grid[i][j-s] == '*' and grid[i+s][j+s] == '*' and grid[i+s][j-s] == '*' and grid[i-s][j+s] == '*' and grid[i-s][j-s] == '*':
                        grid[i+s][j] = '.'  # right
                        grid[i-s][j] = '.'  # left
                        grid[i][j+s] = '.'  # up
                        grid[i][j-s] = '.'  # down
                        grid[i+s][j+s] = '.'  # right up
                        grid[i+s][j-s] = '.'  # right down
                        grid[i-s][j+s] = '.'  # left up
                        grid[i-s][j-s] = '.'  # left down
                        s += 1
                    else:
                        break
                print(i+1, j+1, s-1)
    if k == 0:
        print(-1)


n,m = map(int,input().split())
grid = []
for i in range(n):
    grid.append(list(input()))
stars(n,m,grid)
