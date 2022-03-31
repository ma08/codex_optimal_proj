n, r = map(int, input().split())

a = []
b = []

for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

dp = [0] * (r + 1)

for i in range(n):
    for j in range(r, a[i] - 1, -1):
        if j >= a[i]:
            dp[j] = max(dp[j], dp[j - a[i]] + b[i])

print(max(dp))
