'''

s = input()
t = input()

def get_lcs(s,t):
    # Create a DP matrix
    dp = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
    
    # Populate the matrix
    for i in range(1, len(t)+1):
        for j in range(1, len(s)+1):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[-1][-1]

'''

def get_lcs(s,t):
    # Create a DP matrix
    dp = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
    print(dp)
    # Populate the matrix
    for i in range(1, len(t)+1):
        for j in range(1, len(s)+1):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp)
    return dp[-1][-1]

get_lcs("ABCDGH", "AEDFHR")
print(len(s) - get_lcs(s,t))
