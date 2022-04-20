import sys
sys.setrecursionlimit(10**9)


n, k = map(int, input().split())
a = list(map(int, input().split()))[1:]
memo = [0] * (n + 1)

def dfs(cur):
    if cur == n - 1:
        return 0
    if memo[cur] != 0:
        return memo[cur]
    memo[cur] = max(dfs(cur + 1), dfs(cur + 2)) + a[cur]
    return memo[cur]

print(dfs(0))
