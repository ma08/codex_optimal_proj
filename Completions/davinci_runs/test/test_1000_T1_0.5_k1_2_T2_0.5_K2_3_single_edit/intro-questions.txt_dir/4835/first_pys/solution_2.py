

import sys
import math
from collections import deque

def main():
    t, n, m = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                sx, sy = i, j
                break
    queue = deque()
    queue.append((sx, sy, 0))
    visited = [[False] * m for _ in range(n)]
    visited[sx][sy] = True
    while queue:
        x, y, d = queue.popleft()
        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            print(d)
            return
        if d == t:
            print("NOT POSSIBLE")
            return
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if visited[nx][ny] or grid[nx][ny] == '1':
                continue
            if grid[nx][ny] == 'U' and dy == 1:
                continue
            if grid[nx][ny] == 'D' and dy == -1:
                continue
            if grid[nx][ny] == 'L' and dx == 1:
                continue
            if grid[nx][ny] == 'R' and dx == -1:
                continue
            visited[nx][ny] = True
            queue.append((nx, ny, d + 1))

if __name__ == "__main__":
    main()