

inp = input()
sub = input()

dp = [[0 for _ in range(len(inp)+1)] for _ in range(len(sub)+1)]

for i in range(1, len(sub)+1):
    for j in range(1, len(inp)+1):
        if sub[i-1] == inp[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(len(sub) - dp[-1][-1])
