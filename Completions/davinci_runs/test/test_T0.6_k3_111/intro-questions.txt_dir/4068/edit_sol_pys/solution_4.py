
import sys

n, m = map(int, input().split())
a = [int(input()) for _ in range(m)] 

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

print(solve(n, a))

# 累積和とかにすればもっと速くなるかも？
