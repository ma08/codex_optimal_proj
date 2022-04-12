n, m = [int(i) for i in input().split()]

grid = []
for i in range(n):
    grid.append(input())

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'V':
            if i-1 >= 0:
                if grid[i-1][j] == '.':
                    grid[i-1] = grid[i-1][:j] + "V" + grid[i-1][j+1:]
                if grid[i-1][j] == '#':
                    if (j-1 >= 0) and (grid[i][j-1] == '.'):
                        grid[i] = grid[i][:j-1] + "V" + grid[i][j:]
                    if (j+1 < m) and (grid[i][j+1] == '.'):
                        grid[i] = grid[i][:j+1] + "V" + grid[i][j+2:]

for i in range(n):
    print(grid[i])
