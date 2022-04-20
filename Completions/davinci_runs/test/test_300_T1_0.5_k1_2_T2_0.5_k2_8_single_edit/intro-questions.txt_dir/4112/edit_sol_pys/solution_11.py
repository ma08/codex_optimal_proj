

n, k = map(int, input().split())
a = list(map(int, input().split()))

# print(n, k)
# print(a)

dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = max(dp[i - 1], dp[i - k] + a[i - 1])
    # print(dp)
