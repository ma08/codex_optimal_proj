import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
broken = set(map(int, [input() for _ in range(m)]))
def dfs(i):
    if i == 0:
        return 1
    if i < 0:
        return 0
    if dp[i] != -1:
        return dp[i]
    if i in broken or (i-1) in broken and (i-2) in broken:
        return 0
    dp[i] = dfs(i-1) + dfs(i-2)
    return dp[i]


dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    if i in broken or (i-1) in broken and (i-2) in broken:
        continue
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 1000000007)
