from sys import stdin
from collections import deque


def bfs(grid, start):
    n, m = len(grid), len(grid[0])
    queue = deque([start])
    grid[start[0]][start[1]] = '#'
    while queue:
        r, c = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '.':
                grid[nr][nc] = '#'
                queue.append((nr, nc))

n, m = map(int, stdin.readline().split())
grid = [list(stdin.readline().strip()) for _ in range(n)]

for r in range(n):
    for c in range(m):
        if grid[r][c] == '.':
            grid[r][c] = 'E'
            bfs(grid, (r, c))
            break

for row in grid:
    print ''.join(row)
