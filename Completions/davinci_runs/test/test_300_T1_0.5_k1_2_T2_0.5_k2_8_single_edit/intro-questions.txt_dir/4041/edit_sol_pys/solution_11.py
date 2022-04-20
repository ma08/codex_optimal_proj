

inp = input()
sub = input()

dp = [[0 for _ in range(len(sub)+1)] for _ in range(len(inp)+1)] # dp[i][j] = length of longest common subsequence of inp[:i] and sub[:j]

for i in range(1, len(inp)+1):
    for j in range(1, len(sub)+1):
        if inp[i-1] == sub[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1 # inp[i-1] and sub[j-1] are in the LCS
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # inp[i-1] and sub[j-1] are not in the LCS

print(len(inp) - dp[-1][-1]) # number of deletions to make inp a subsequence of sub
