

import sys
from collections import deque

def get_star_size(r, c):
    s = 1
    while r+s < n and c+s < m and grid[r+s][c+s] == '*' and grid[r-s][c-s] == '*' and grid[r+s][c-s] == '*' and grid[r-s][c+s] == '*': s += 1
    return s

def is_valid(r, c, s):
    for i in range(r-s+1, r+s):
        for j in range(c-s+1, c+s):
            if grid[i][j] == '.': return False
    return True

def check_star(r, c):
    s = 1
    while r+s < n and c+s < m and grid[r+s][c+s] == '*' and grid[r-s][c-s] == '*' and grid[r+s][c-s] == '*' and grid[r-s][c+s] == '*': s += 1
    return s-1

def bfs(r, c):
    s = 1
    if grid[r][c] == '.': return 0
    q = deque()
    q.append((r, c, s))
    while q:
        r, c, s = q.popleft()
        if is_valid(r, c, s):
            for i in range(r-s+1, r+s):
                for j in range(c-s+1, c+s):
                    grid[i][j] = '.'
                stars.append((r, c, s))
                for x, y in [(r, c+s), (r, c-s), (r+s, c), (r-s, c)]:
                    if x < n and x >= 0 and y < m and y >= 0:
                        q.append((x, y, check_star(x, y)))
    return

n, m = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
    grid.append(list(sys.stdin.readline().strip()))

stars = []

for i in range(n):
    for j in range(m):
        if grid[i][j] == '*':
            s = get_star_size(i, j)
            if is_valid(i, j, s):
                for k in range(i-s+1, i+s):
                    for l in range(j-s+1, j+s):
                        grid[k][l] = '.'
                stars.append((i, j, s))

for i in range(n):
    for j in range(m):
        if grid[i][j] == '*':
            bfs(i, j)

print(len(stars))
for r, c, s in stars:
    print(r+1, c+1, s)