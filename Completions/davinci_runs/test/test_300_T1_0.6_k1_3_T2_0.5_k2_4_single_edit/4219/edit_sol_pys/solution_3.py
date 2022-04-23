
n = int(input())
a = [0] * n
x = [[0] * n for _ in range(n)]
y = [[0] * n for _ in range(n)]
for i in range(n):
    a[i] = int(input())
    for _ in range(a[i]):
        xi, yi = map(int, input().split())
        x[i][xi - 1] = 1
        y[i][xi - 1] = yi

def dfs(i, honest):
    if dp[i][honest] != -1:
        return dp[i][honest]
    ret = 0
    if honest:
        for j in range(a[i]):
            if y[i][j] == 1:
                ret = max(ret, dfs(j, 1))
            else:
                ret = max(ret, dfs(j, 1) + dfs(j, 0))
    else:
        ret = 1
        for j in range(a[i]):
            if y[i][j] == 1:
                ret = max(ret, dfs(j, 1) + dfs(j, 0))
            else:
                ret = max(ret, dfs(j, 0))
    dp[i][honest] = ret
    return ret

dp = [[-1] * 2 for _ in range(n)]
ret = 0
for i in range(n):
    ret = max(ret, dfs(i, 1) + dfs(i, 0))
print(ret)
