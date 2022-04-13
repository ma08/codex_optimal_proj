
#%%
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(v):
    if v == n:
        return 0
    if dp[v] != -1:
        return dp[v]
    if v + a[v] <= n:
        dp[v] = dfs(v+a[v]) + 1
        return dp[v]
    else:
        dp[v] = 0
        return dp[v]

n = int(input())
a = list(map(int, input().split()))
dp = [-1]*n
print(dfs(0))
