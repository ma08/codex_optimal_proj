
import sys
sys.setrecursionlimit(10**6)

def dfs(i, j):
    if board[i][j] == 0:
        return 0
    board[i][j] = 0
    count = 1
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == 0 and dj == 0:
                continue
            ni = i + di
            nj = j + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            count += dfs(ni, nj)
    return count

N = int(input())
M = int(input())
board = [[0] * M for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        board[i][j] = row[j]

ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans, dfs(i, j))
print(ans)
