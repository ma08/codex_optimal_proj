import sys

def main():
    s = sys.stdin.readline().strip() # read a line with a single integer
    t = sys.stdin.readline().strip() # read a list of integers, 2 in this case

    n = len(s) # lenght of s
    m = len(t) # length of t

    dp = [[0 for j in range(m + 1)] for i in range(n + 1)] # dp array

    for i in range(1, n + 1): # iterate over s
        for j in range(1, m + 1): # iterate over t
            if s[i - 1] == t[j - 1]: # if the characters match
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j]) # max of diagonal + 1 or previous
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # max of previous or previous

    print(n - dp[n][m]) # print the number of characters to delete

if __name__ == '__main__':
    main()
