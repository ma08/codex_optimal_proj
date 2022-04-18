import sys
sys.setrecursionlimit(10**7)


n = int(input())
a = [0] + [int(input()) for _ in range(n)]
x = [[0 for _ in range(a[i]+1)] for i in range(n+1)]
y = [[0 for _ in range(a[i]+1)] for i in range(n+1)]
for i in range(n):
    for j in range(a[i]):
        x[i][j+1], y[i][j+1] = map(int, input().split())
        x[i][j+1] -= 1

def dfs(i, honest, dp):
    if dp[i][honest] > -1:
        return dp[i][honest] 
    ret = 0
    if honest:
        for j in range(1, a[i]+1):
            if y[i][j] == 1:
                ret = max(ret, dfs(x[i][j], 1, dp))
            else:
                ret = max(ret, dfs(x[i][j], 1, dp) + dfs(x[i][j], 0, dp))
    else:
        ret = 0
        for j in range(1, a[i]+1):
            if y[i][j] == 1:
                ret = max(ret, dfs(x[i][j], 1, dp) + dfs(x[i][j], 0, dp))
            else:
                ret = max(ret, dfs(x[i][j], 0, dp))
    dp[i][honest] = ret
    #print(dp)
    return ret

dp = [[-1 for _ in range(2)] for _ in range(n+1)]
ret = 0
for i in range(n+1):
    ret = max(ret, dfs(i, 1, dp) + dfs(i, 0, dp))
print(ret)
