# Solution

a, n, m = map(int, input().split())

l = [0] * n
r = [0] * n

for i in range(n):
    l[i], r[i] = map(int, input().split())

x = [0] * m
p = [0] * m

for i in range(m):
    x[i], p[i] = map(int, input().split())

dp = [0] * (a + 1)

for i in range(a):
    dp[i + 1] = dp[i] + 1
    for j in range(m):
        if x[j] <= i:
            dp[i + 1] = min(dp[i + 1], dp[i] + p[j])

for i in range(n):
    if dp[l[i]] == dp[r[i]]:
        print(-1)
        exit()

print(dp[a])
