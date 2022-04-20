

def main():
    # read data for 2 sequences
    s = list(input())
    t = list(input())
    n = len(s)
    m = len(t)
    # create a 2-dimensional array to store the length of the longest common subsequence
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    # print(dp)
    # print(dp[n][m])
    # create a stack to store the longest common subsequence
    stack = []
    i = n
    j = m
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            stack.append(s[i-1])
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i-1][j]:
                i -= 1
            else:
                j -= 1
    # print(stack)
    # output the result
    stack.reverse()
    print(''.join(stack))

main()
