for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = max(a[0], 0)
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + a[i], max(a[i], 0))
    print(max(dp) if max(dp) > 0 else max(a))
