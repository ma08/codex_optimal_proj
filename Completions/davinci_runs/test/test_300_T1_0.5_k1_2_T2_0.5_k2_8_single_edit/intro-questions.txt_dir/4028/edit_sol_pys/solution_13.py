

import sys
import math

def main():
    n = int(input())
    s = input()
    l = len(s)
    dp = [[0] * (n+1) for i in range(l+1)]
    ans = 0
    for i in range(l):
        if s[i] == '(':
            dp[i][0] = 1
    for i in range(l):
        for j in range(n):
            dp[i+1][j] += dp[i][j]
            if s[i] == '(':
                dp[i+1][j+1] += dp[i][j]
            elif j > 0:
                dp[i+1][j-1] += dp[i][j]
    for i in range(n+1):
        ans += dp[l][i]
    print(ans)

if __name__ == "__main__":
    main()
