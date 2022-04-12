

from sys import stdin

n, m = map(int, stdin.readline().split())
grid = [list(stdin.readline().strip()) for i in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            grid[i][j] = '#'
            if i > 0 and grid[i-1][j] == '.':
                grid[i-1][j] = 'E'
            if i < n-1 and grid[i+1][j] == '.':
                grid[i+1][j] = 'E'
            if j > 0 and grid[i][j-1] == '.':
                grid[i][j-1] = 'E'
            if j < m-1 and grid[i][j+1] == '.':
                grid[i][j+1] = 'E'

for row in grid:
    print(''.join(row))
