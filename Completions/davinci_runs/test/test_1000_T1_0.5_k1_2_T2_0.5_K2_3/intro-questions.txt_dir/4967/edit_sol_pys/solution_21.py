
import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, z):
    q = deque()
    q.append([x, y, z])
    while q:
        x, y, z = q.popleft()
        if x == n - 1 and y == m - 1:
            return z
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0:
                q.append([nx, ny, z + 1])
                a[nx][ny] = 1
    return -1

n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]

print(bfs(0, 0, 1))
