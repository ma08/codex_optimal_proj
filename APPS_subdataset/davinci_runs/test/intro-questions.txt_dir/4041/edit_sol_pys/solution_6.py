import sys

def main():
    s = sys.stdin.readline().strip().split()
    t = sys.stdin.readline().strip().split()

    n = len(s[0])
    m = len(t[0])

    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[0][i - 1] == t[0][j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(n - dp[n][m])

if __name__ == '__main__':
    main()
