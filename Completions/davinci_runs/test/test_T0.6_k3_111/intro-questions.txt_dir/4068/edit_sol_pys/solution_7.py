
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]

def solve(n, a):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        if i in a: dp[i] = 0
    return dp[n] % (10**9 + 7)

print(solve(n, a))

# 累積和とかにすればもっと速くなるかも？
