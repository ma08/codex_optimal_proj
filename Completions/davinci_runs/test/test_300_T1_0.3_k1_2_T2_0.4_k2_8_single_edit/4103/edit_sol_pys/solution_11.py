

def max_segments(n, b, a, s, dp):
    if n <= 0:
        return 0
    if n in dp:
        return dp[n]
    if n == 1:
        if s[0] >= b:
            dp[n] = 1
        else:
            dp[n] = 0
        return dp[n]
    if n == 2:
        if s[1] >= b and s[0] >= b:
            dp[n] = 2
        elif s[1] >= b and s[0] < b:
            dp[n] = 1
        elif s[1] < b and s[0] >= b:
            dp[n] = 1
        else:
            dp[n] = 0
        return dp[n]
    if s[n - 1] >= b:
        dp[n] = max_segments(n - 1, b, a, s, dp) + 1
    elif s[n - 1] < b and s[n - 2] >= b:
        dp[n] = max_segments(n - 2, b, a, s, dp) + 1
    else:
        dp[n] = max_segments(n - 1, b, a, s, dp)
    return dp[n]


n, b, a = map(int, input().split())
s = list(map(int, input().split()))
dp = {}
print(max_segments(n, b, a, s, dp))
