

def max_segments(n, b, a, s, dp):
    # TODO: Write your code here
    if n == 0:
        return 0
    if dp[n][b][a] == -1:
        if s[n - 1] == 0:
            if b > 0:
                dp[n][b][a] = max(dp[n][b][a], max_segments(n - 1, b - 1, a, s, dp) + 1)
            if a > 0:
                dp[n][b][a] = max(dp[n][b][a], max_segments(n - 1, b, a - 1, s, dp) + 1)
        else:
            if a > 0:
                dp[n][b][a] = max(dp[n][b][a], max_segments(n - 1, b, a - 1, s, dp) + 1)
            else:
                dp[n][b][a] = max(dp[n][b][a], max_segments(n - 1, b, a, s, dp))
    return dp[n][b][a]


n, b, a = map(int, input().split())
s = list(map(int, input().split()))
dp = [[[-1 for _ in range(a + 1)] for _ in range(b + 1)] for _ in range(n + 1)]
print(max_segments(n, b, a, s, dp))
