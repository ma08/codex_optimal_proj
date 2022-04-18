

import sys
import math

def main():
    n = int(input())
    s = input()
    s_len = len(s)
    dp = [[0] * (n + 1) for i in range(s_len + 1)]
    ans = 0
    for i in range(s_len):
        if s[i] == '(':
            dp[i][0] = 1
    for i in range(s_len):
        for j in range(n):
            if dp[i][j] == 0:
                continue
            if s[i] == '(':
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j + 1] += dp[i][j]
            else:
                if j > 0:
                    dp[i + 1][j - 1] += dp[i][j]
    for i in range(n + 1):
        ans += dp[s_len][i]
    print(ans)

if __name__ == "__main__":
    main()
