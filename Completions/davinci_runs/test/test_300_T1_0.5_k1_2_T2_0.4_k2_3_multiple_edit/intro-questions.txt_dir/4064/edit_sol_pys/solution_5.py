
n, h, l, r = map(int, input().split())
a = list(map(int, input().split())) 

t = [0]
for i in range(n):
    t.append(t[i] + a[i])

dp = [[0] * (h+1) for _ in range(n+1)]

for i in range(n):
    for j in range(h):
        dp[i+1][j] = max(dp[i][j], dp[i][(j-a[i])%h] + 1 if l <= (j-a[i])%h <= r else 0)

print(max(dp[n]))
