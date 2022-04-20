

from sys import stdin
from collections import deque

def main():
    n, m, k = map(int, stdin.readline().split())
    a = [list(map(int, stdin.readline().split())) for _ in range(n)]

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    dp2 = [[0] * (m + 1) for _ in range(n + 1)]
    dp2[1][1] = a[0][0]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            dp2[i][j] = dp2[i - 1][j] ^ dp2[i][j - 1] ^ a[i - 1][j - 1]

    ans = 0
    q = deque([(0, 0, k)])
    visited = [[[False] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    visited[0][0][k] = True
    while q:
        i, j, prev = q.popleft()
        if i == n - 1 and j == m - 1:
            ans += dp[i + 1][j + 1]
            continue
        ni, nj = i + 1, j + 1
        if ni < n:
            nk = prev ^ a[ni][j]
            if not visited[ni][j][nk]:
                visited[ni][j][nk] = True
                q.append((ni, j, nk))
        if nj < m:
            nk = prev ^ a[i][nj]
            if not visited[i][nj][nk]:
                visited[i][nj][nk] = True
                q.append((i, nj, nk))

    print(ans)

main()