import sys
sys.setrecursionlimit(10**6)


def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return
    if a[i][j] == '#':
        return
    if dp[i][j] != -1:
        return
    dp[i][j] = 1
    for k in range(4):
        dfs(i + dx[k], j + dy[k])


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if a[i][j] == 's':
            dfs(i, j)

for i in range(n):
    for j in range(m):
        if a[i][j] == 'g':
            if dp[i][j] == 1:
                print('Yes')
            else:
                print('No')


'''
n = int(input())
a = list(map(int, input().split()))

def solve(n, s):
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                res += 1
    return res

print(solve(n, a))
'''
