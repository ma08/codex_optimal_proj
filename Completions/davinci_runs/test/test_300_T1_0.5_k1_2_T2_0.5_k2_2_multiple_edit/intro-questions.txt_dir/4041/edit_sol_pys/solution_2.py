
inp = input()
sub = input()

# Initialize a 2d array of size len(inp) + 1 x len(sub) + 1.
# Each element represents the length of the longest subsequence of sub in a substring of inp.
dp = [[0 for _ in range(len(sub)+1)] for _ in range(len(inp)+1)]

for i in range(1, len(inp)+1):
    for j in range(1, len(sub)+1):
        if inp[i-1] == sub[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(len(inp) - dp[-1][-1])
