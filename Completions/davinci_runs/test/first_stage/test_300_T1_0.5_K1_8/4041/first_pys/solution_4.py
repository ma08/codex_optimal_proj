

s = input()
t = input()

dp = [[0 for i in range(len(s))] for j in range(len(t))]

for i in range(len(t)):
    for j in range(len(s)):
        if i == 0 and j == 0:
            if t[i] == s[j]:
                dp[i][j] = 1
            else:
                dp[i][j] = 0
        elif i == 0:
            if t[i] == s[j]:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1]
        elif j == 0:
            if t[i] == s[j]:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j]
        else:
            if t[i] == s[j]:
                dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

print(len(s)-dp[-1][-1])