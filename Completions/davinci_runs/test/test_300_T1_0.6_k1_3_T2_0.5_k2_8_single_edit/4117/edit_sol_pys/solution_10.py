

import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y, cnt):
    if x == N-1 and y == N-1:
        global ans
        ans = min(ans, cnt)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < N and 0 <= ny and ny < N and visited[nx][ny] == 0:
            if arr[nx][ny] == 1:
                visited[nx][ny] = 1
                dfs(nx, ny, cnt+1)
                visited[nx][ny] = 0
            else:
                visited[nx][ny] = 1
                dfs(nx, ny, cnt)
                visited[nx][ny] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans = float('inf')

visited[0][0] = 1
dfs(0, 0, 1)
print(ans)
