
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

dp = [[0 for i in range(m+1)] for j in range(n)]

print(dp[n][m])
