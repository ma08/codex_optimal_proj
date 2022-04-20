

def max_segments(n, b, a, s, dp):
    # TODO: Write your code here
    if n == 0:
        return 0
    if dp[n][b][a] == -1:
        if b == 0 and a == 0:
            dp[n][b][a] = 0
        elif b == 0:
            dp[n][b][a] = max_segments(n - 1, b, a - 1, s, dp)
        elif a == 0:
            dp[n][b][a] = max_segments(n - 1, b - 1, a, s, dp)
        else:
            dp[n][b][a] = max(max_segments(n - 1, b - 1, a, s, dp), max_segments(n - 1, b, a - 1, s, dp))
        if s[n - 1] == 1:
            dp[n][b][a] += 1
    return dp[n][b][a]


n, b, a = map(int, input().split())
s = list(map(int, input().split()))
print(max_segments(n, b, a, s))
