

n, m = [int(i) for i in input().split()]

grid = []
for i in range(n):
    grid.append(input())

#print(grid)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'V':
            if i-1 >= 0:
                if grid[i-1][j] == '.':
                    grid[i-1] = grid[i-1][:j] + "V" + grid[i-1][j+1:]
                elif grid[i-1][j] == '#':
                    if (j-1 >= 0) and (grid[i][j-1] == '.'):
                        grid[i] = grid[i][:j-1] + "V" + grid[i][j:]
                    if (j+1 < m) and (grid[i][j+1] == '.'):
                        grid[i] = grid[i][:j+1] + "V" + grid[i][j+2:]
            elif i+1 < n:
                if grid[i+1][j] == '.':
                    grid[i+1] = grid[i+1][:j] + "V" + grid[i+1][j+1:]
                elif grid[i+1][j] == '#':
                    if (j-1 >= 0) and (grid[i][j-1] == '.'):
                        grid[i] = grid[i][:j-1] + "V" + grid[i][j:]
                    if (j+1 < m) and (grid[i][j+1] == '.'):
                        grid[i] = grid[i][:j+1] + "V" + grid[i][j+2:]
            if j-1 >= 0:
                if grid[i][j-1] == '.':
                    grid[i] = grid[i][:j-1] + "V" + grid[i][j:]
                elif grid[i][j-1] == '#':
                    if (i-1 >= 0) and (grid[i-1][j] == '.'):
                        grid[i-1] = grid[i-1][:j] + "V" + grid[i-1][j+1:]
                    if (i+1 < n) and (grid[i+1][j] == '.'):
                        grid[i+1] = grid[i+1][:j] + "V" + grid[i+1][j+1:]
            elif j+1 < m:
                if grid[i][j+1] == '.':
                    grid[i] = grid[i][:j+1] + "V" + grid[i][j+2:]
                elif grid[i][j+1] == '#':
                    if (i-1 >= 0) and (grid[i-1][j] == '.'):
                        grid[i-1] = grid[i-1][:j] + "V" + grid[i-1][j+1:]
                    if (i+1 < n) and (grid[i+1][j] == '.'):
                        grid[i+1] = grid[i+1][:j] + "V" + grid[i+1][j+1:]

for i in range(n):
    print(grid[i])
