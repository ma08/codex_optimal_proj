

# TODO: WA

import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    mod = 1000000007
    # dp[i][j] = number of sequences ending with j, i-th bracket matches,
    # where i is the number of brackets, j is the number of '('
    dp = [[0 for i in range(len(s)+1)] for j in range(2*n+1)]
    dp[0][0] = 1
    for i in range(1, 2*n+1):
        for j in range(len(s)+1):
            if i-1-j < 0 or 2*n-i < j:
                continue
            if dp[i-1][j] > 0:
                if s[j] == '(':
                    dp[i][j+1] = (dp[i][j+1] + dp[i-1][j]) % mod
                else:
                    dp[i][j] = (dp[i][j] + dp[i-1][j]) % mod
                    dp[i][j+2] = (dp[i][j+2] + dp[i-1][j]) % mod
    ans = dp[2*n][len(s)] % mod
    print(ans)
