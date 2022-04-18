

import sys
import math

def main():
    n = int(input())
    s = input()
    l = len(s)
    dp = [[0] * (n+1) for j in range(l+1)]
    ans = 0
    for i in range(l):
        if s[i] == '(':
            dp[i][0] = 1
    for i in range(l):
        for k in range(n):
            if dp[i][k] == 0:
                continue
            if s[i] == '(':
                dp[i+1][k] += dp[i][k]
                dp[i+1][k+1] += dp[i][k]
            else:
                if k > 0:
                    dp[i+1][k-1] += dp[i][k]
    for i in range(n+1):
        ans += dp[l][i]
    print(ans)

if __name__ == "__main__":
    main()
