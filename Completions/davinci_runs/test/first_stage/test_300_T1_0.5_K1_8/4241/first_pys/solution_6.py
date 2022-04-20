

# My Answer
def minimum_change_number(s, t):
    s_len = len(s)
    t_len = len(t)
    dp = [[0 for _ in range(t_len+1)] for _ in range(s_len+1)]
    for i in range(s_len+1):
        for j in range(t_len+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return dp[s_len][t_len]

if __name__ == "__main__":
    s = input()
    t = input()
    print(minimum_change_number(s, t))