import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

def solve(a, m, n):
    dp = [0] * (m + 1)
    dp[0] = 1
    for x in a:
        for i in range(m, x - 1, -1):
            dp[i] += dp[i - x]
    return dp[m]

print(solve(a, m, n))
