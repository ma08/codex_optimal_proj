from collections import deque


def bfs(i):
    q = deque([(i, 0)])
    while q:
        v, d = q.popleft()
        if d > 2:
            return False
        for u in g[v]:
            if u == i:
                return True
            if not used[u]:
                used[u] = True
                q.append((u, d + 1))
    return False

def dfs(i, honest):
    if dp[i][honest] != -1:
        return dp[i][honest]
    ret = 0
    if honest:
        for j in range(a[i]):
            if y[i][j] == 1:
                ret = max(ret, dfs(x[i][j], 1))
            else:
                ret = max(ret, dfs(x[i][j], 1) + dfs(x[i][j], 0))
    else:
        ret = 1
        for j in range(a[i]):
            if y[i][j] == 1:
                ret = max(ret, dfs(x[i][j], 1) + dfs(x[i][j], 0))
            else:
                ret = max(ret, dfs(x[i][j], 0))
    dp[i][honest] = ret
    return ret

dp = [[-1 for _ in range(2)] for _ in range(n)]
ret = 0
for i in range(n):
    ret = max(ret, dfs(i, 1) + dfs(i, 0))
print(ret)
