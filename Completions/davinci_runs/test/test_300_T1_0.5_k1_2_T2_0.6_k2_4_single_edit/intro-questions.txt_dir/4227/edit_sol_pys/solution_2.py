
# https://atcoder.jp/contests/abc087/tasks/abc087_b

import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
x = int(input())

ans = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if 500 * i + 100 * j + 50 * k == x:
                ans += 1
print(ans)

n, m = map(int, input().split())
edges = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1] += 1
    edges[b - 1] += 1

def dfs(i, j):
    if i == n:
        return j == 0
    if dp[i][j] != -1:
        return dp[i][j]
    res = dfs(i + 1, j)
    if j - edges[i] >= 0:
        res |= dfs(i + 1, j - edges[i])
    dp[i][j] = res
    return res

dp = [[-1] * (n * (n - 1) // 2 + 1) for _ in range(n)]
ans = 0
for i in range(1, n * (n - 1) // 2 + 1):
    if dfs(0, i):
        ans += 1
print(ans)
