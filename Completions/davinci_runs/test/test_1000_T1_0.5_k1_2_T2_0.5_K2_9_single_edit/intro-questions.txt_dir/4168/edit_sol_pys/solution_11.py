import sys
from collections import deque
input = sys.stdin.readline

def is_safe(i, j):
    return 0 <= i < N and 0 <= j < N

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        i, j = q.popleft()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if not is_safe(ni, nj):
                continue
            if not visited[ni][nj] and G[ni][nj] == 1:
                visited[ni][nj] = True
                q.append((ni, nj))

N = int(input())
G = [[int(x) for x in input().split()] for _ in range(N)]
visited = [[False] * N for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j] and G[i][j] == 1:
            bfs(i, j)
            cnt += 1

print(cnt)

n = int(input())

if n == 0:
    print(0)
    exit()
ans = ""
while n != 0:
    if n % (-2) == 0:
        ans += "0"
        n = n // (-2)
    else:
        ans += "1"
        n = n // (-2) + 1
print(ans[::-1])
