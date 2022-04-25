import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline



def dfs(v, p):
    for u in edges[v]:
        if u == p:


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue
            continue


n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)


dfs(0, -1)

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)


# DP[i][j] = i番目までの頂点を使って、jを含む場合のパターン数
dp = [[0] * (1 << n) for _ in range(n)]
dp[0][1] = 1
for i in range(n - 1):
    for j in range(1 << n):
        if dp[i][j] == 0:
            continue
        for k in range(1, n + 1):
            if j & (1 << k) != 0 or len(edges[k - 1]) == 0:
                continue
            dp[i + 1][j | (1 << k)] += dp[i][j]
print(dp[n - 1][2 ** n - 1])
