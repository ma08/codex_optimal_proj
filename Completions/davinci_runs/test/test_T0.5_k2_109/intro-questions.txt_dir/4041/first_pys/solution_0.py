

import sys

def main():
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()

    n = len(s)
    m = len(t)

    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(n - dp[n][m])

if __name__ == '__main__':
    main()