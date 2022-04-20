

#-----Solution-----

#This is a solution for the problem, but it is too slow.
def solution(string):
    string = string.replace('?', 'abc')
    total = 0
    for i in string:
        for j in string:
            for k in string:
                if i+j+k == 'abc':
                    total += 1
    return total

#This is the solution for the problem.
def solution(s):
    n = len(s)
    mod = 10**9 + 7
    dp = [[0] * 3 for _ in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        if s[i] == '?':
            dp[i][0] = dp[i - 1][0] * 3
            dp[i][1] = dp[i - 1][0] + dp[i - 1][1] * 3
            dp[i][2] = dp[i - 1][1] + dp[i - 1][2] * 3
        elif s[i] == 'a':
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = dp[i - 1][0]
            dp[i][2] = dp[i - 1][1]
        elif s[i] == 'b':
            dp[i][0] = 0
            dp[i][1] = dp[i - 1][0]
            dp[i][2] = dp[i - 1][1]
        elif s[i] == 'c':
            dp[i][0] = 0
            dp[i][1] = 0
            dp[i][2] = dp[i - 1][1]
    return dp[-1][2] % mod