
 
n, m = [int(i) for i in input().split()]

grid = []
for i in range(n):
    grid.append(input())

print(grid)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'v':
            if i-1 >= 0:
                grid[i-1] = grid[i-1][:j] + "v" + grid[i-1][j+1:]
            elif i+1 < n:
                if grid[i+1][j] == '.':
                    grid[i+1] = grid[i+1][:j] + "v" + grid[i+1][j+1:]
            if j-1 >= 0:
                if grid[i][j-1] == '.':
                    grid[i] = grid[i][:j-1] + "v" + grid[i][j:]
            elif j+1 < m:
                if grid[i][j+1] == '.':
                    grid[i] = grid[i][:j+1] + "v" + grid[i][j+2:]

for i in range(n):
    print(grid[i])
