

n = int(input())
s = input()

def is_regular(s):
    if s == "":
        return True
    if s[0] == "(":
        i = 1
        while i < len(s) and s[i] == "(":
            i += 1
        if i < len(s) and s[i] == ")":
            return is_regular(s[1:i]) and is_regular(s[i+1:])
    return False

if is_regular(s):
    print(0)
    exit()

dp = [[0]*n for _ in range(n)]
for i in range(n):
    if s[i] == ")":
        dp[i][i] = 1

for size in range(2, n+1):
    for i in range(n-size+1):
        j = i+size-1
        if s[i] == "(":
            dp[i][j] = dp[i+1][j]
        elif s[j] == ")":
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]

print(dp[0][n-1])