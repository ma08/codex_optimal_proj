# coding: utf-8

import sys

def solve(s):
    dp = [0] * len(s)
    for i in range(len(s)):
        if s[i] == 'R':
            dp[i] = 0
        else:
            dp[i] = dp[i - 1] + 1
    return max(dp)

def main():
    s = sys.stdin.readline().strip()
    print(solve(s))

if __name__ == '__main__':
    main()
