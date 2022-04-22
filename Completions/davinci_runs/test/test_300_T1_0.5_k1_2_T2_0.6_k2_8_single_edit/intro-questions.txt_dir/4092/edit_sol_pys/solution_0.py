

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 1
    for i in range(1, m + 1):
        for j in range(n + 1):
            if j - A[i - 1] >= 0:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - A[i - 1]]) % 1000000007
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[m][n])

if __name__ == '__main__':
    main()
