import sys
sys.setrecursionlimit(10 ** 7)

n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

dp = [[-1, -1] for i in range(n)]


def dfs(i):
    if dp[i][0] != -1:
        return dp[i]
    if i == 0:
        if a[i] > l and a[i] < r:
            dp[i][0] = 1
        else:
            dp[i][0] = 0
        if a[i] - 1 > l and a[i] - 1 < r:
            dp[i][1] = 1
        else:
            dp[i][1] = 0
    else:
        dp[i][0] = max(dfs(i - 1)[0], dfs(i - 1)[1])
        if a[i] > l and a[i] < r:
            dp[i][0] += 1
        dp[i][1] = max(dfs(i - 1)[0], dfs(i - 1)[1])
        if a[i] - 1 > l and a[i] - 1 < r:
            dp[i][1] += 1
    return dp[i]


print(max(dfs(n - 1)[0], dfs(n - 1)[1]))
