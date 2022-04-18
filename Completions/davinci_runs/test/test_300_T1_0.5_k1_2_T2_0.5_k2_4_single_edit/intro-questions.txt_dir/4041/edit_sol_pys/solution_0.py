
inp = input()
sub = input()

dp = [[0 for _ in range(len(sub)+1)] for _ in range(len(inp)+1)]

for i in range(1, len(inp)+1):
    for j in range(1, len(sub)+1):
        if inp[i-1] == sub[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1  # add 1 to the previous longest subsequence
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # take the max of the previous row and column

print(len(inp) - dp[-1][-1])
