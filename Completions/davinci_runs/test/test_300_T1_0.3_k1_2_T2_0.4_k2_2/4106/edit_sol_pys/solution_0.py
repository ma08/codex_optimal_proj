import sys
sys.setrecursionlimit(10**6)

def dfs(i, j):
    if dp[i][j] >= 0:
        return dp[i][j]
    if j == 0:
        dp[i][j] = 0
    elif i < k:
        dp[i][j] = -1
    else:
        dp[i][j] = max(dfs(i-1, j), dfs(i-k, j-1) + a[i-1])
    return dp[i][j]


def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[-1]*(x+1) for _ in range(n+1)]
    print(dfs(n, x))

main()
