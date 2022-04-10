

import sys

def solve(n, h, l, r, a):
    # dp[i][j] is the max number of good sleeping times if Vova goes to sleep after a[i] hours for the next j times.
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(n, i - 1, -1):
            # Case 1: Vova goes to sleep after a[i] hours
            t = (a[i] + h - 1) % h
            dp[i][j] = dp[i + 1][j - 1] + (1 if l <= t <= r else 0)
            # Case 2: Vova goes to sleep after a[i] - 1 hours
            t = (a[i] - 1 + h - 1) % h
            dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + (1 if l <= t <= r else 0))
    return dp[0][n]

def main():
    n, h, l, r = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    print(solve(n, h, l, r, a))

if __name__ == '__main__':
    main()