
def problem_D():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        dp[i + 1] = dp[i] * 2 % 1000000007
    ans = 0
    for i in range(n):
        if a[i] == 0:
            continue
        if i + 1 < k:
            ans += dp[i]
        elif i + 1 == k:
            ans += dp[i] * 2
        else:
            ans += dp[i] * 2 - dp[i - k]
    print(ans % 1000000007)

problem_D()
