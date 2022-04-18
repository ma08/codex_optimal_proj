

import sys
import math

def main():
    n = int(input())
    s = input()
    l = len(s)
    dp = [0] * (n+1)
    dp[0] = 1
    ans = 0
    for i in range(l):
        ndp = [0] * (n+1)
        for j in range(n+1):
            if s[i] == '(':
                ndp[j] += dp[j]
                ndp[j+1] += dp[j]
            else:
                if j > 0:
                    ndp[j-1] += dp[j]
        dp = ndp
    for i in range(n+1): ans += dp[i]
    print(ans)

if __name__ == "__main__":
    main()
