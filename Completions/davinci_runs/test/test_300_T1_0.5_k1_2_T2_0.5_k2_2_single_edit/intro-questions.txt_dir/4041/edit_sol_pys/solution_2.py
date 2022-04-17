

inp = input().split()
sub = input().split()

inp_len = len(inp)
sub_len = len(sub)

dp = [[0 for _ in range(sub_len+1)] for _ in range(inp_len+1)]

for i in range(1, inp_len+1):
    for j in range(1, sub_len+1):
        if inp[i-1] == sub[j-1]: dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(len(inp) - dp[-1][-1])
