

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    dp = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(n - dp[n-1][m-1])

if __name__ == '__main__':
    main()