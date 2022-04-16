#!/usr/bin/env python3

import sys

def main():
    s = sys.stdin.readline().strip()
    n = len(s)
    dp = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 1
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                dp[i][j] = 1
    ans = 0
    for i in range(n):
        for j in range(n):
            if dp[i][j] == 1:
                ans = max(ans, j - i + 1)
    print(ans)


if __name__ == '__main__':
    main()
