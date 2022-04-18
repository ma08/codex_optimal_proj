from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
grid = []
for _ in range(n):
    grid.append(stdin.readline().strip())

# Breadth-first search
# We start from the first land cell and place a coffee shop there.
# Then we check all the adjacent cells. If they are land cells, we place a coffee shop there
# and add them to the queue. We repeat this process until the queue is empty.
q = deque()
q.append((0, 0))
while q:
    i, j = q.popleft()
    if grid[i][j] == '.':
        grid[i] = grid[i][:j] + 'E' + grid[i][j + 1:]
        if i > 0 and grid[i-1][j] == '.':
            q.append((i - 1, j))
        if j > 0 and grid[i][j-1] == '.':
            q.append((i, j - 1))
        if i < n - 1 and grid[i + 1][j] == '.':
            q.append((i + 1, j))
        if j < m - 1 and grid[i][j + 1] == '.':
            q.append((i, j + 1))

print(*grid, sep='\n')
