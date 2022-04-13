#

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * n
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1] + a[i], a[i])
    print(max(dp))
