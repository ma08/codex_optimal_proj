

def dp(string, i):
    if i == len(string):
        return 1
    if string[i] == '+':
        return dp(string, i+1) + dp(string, i+2)
    return dp(string, i+1)

print(dp(input()))
