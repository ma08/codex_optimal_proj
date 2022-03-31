import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 30min

dp = [0] * (r + 1)

for i in range(n):
    for j in range(r, 0, -1):
        if j >= a[i]:
            dp[j] = max(dp[j], dp[j - a[i]] + b[i])

print(max(dp))
