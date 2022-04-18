

import sys

def bfs(grid, x, y):
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i][j] = [grid[i][j], -1]
    q = [[x, y]]
    grid[x][y][1] = 0
    while len(q) > 0:
        a, b = q.pop(0)
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < len(grid) and 0 <= y < len(grid) and grid[x][y][0] != '.' and grid[x][y][1] == -1:
                grid[x][y][1] = grid[a][b][1] + 1
                q.append([x, y])
    return grid

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

grid = []
for i in range(int(sys.stdin.readline().strip())):
    grid.append(list(sys.stdin.readline().strip()))

x = -1
y = -1
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j][0] == 'S':
            x = i
            y = j

grid = bfs(grid, x, y)

ans = -1
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j][0] == 'H':
            ans = max(ans, grid[i][j][1])

print(ans)
