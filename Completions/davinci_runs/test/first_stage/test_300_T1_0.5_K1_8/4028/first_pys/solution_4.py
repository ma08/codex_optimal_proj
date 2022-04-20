

def count(n, s):
    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(0, n + 1):
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]
            dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= 1000000007
    cnt = 0
    for i in range(len(s)):
        if s[i] == "(":
            cnt += 1
        else:
            cnt -= 1
    return dp[n][cnt]

n = int(input())
s = input()
print(count(n, s))