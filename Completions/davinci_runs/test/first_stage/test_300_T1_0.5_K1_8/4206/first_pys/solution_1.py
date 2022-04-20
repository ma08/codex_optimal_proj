

from sys import stdin
from itertools import accumulate

def main():
    s = stdin.readline().strip()
    s = list(map(int, s))
    n = len(s)
    dp = [[0 for j in range(3)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(3):
            dp[i][j] = dp[i - 1][j]
            dp[i][(j + s[i - 1]) % 3] += 1
    ans = 0
    for i in range(n):
        ans += dp[i][0] * (dp[n][0] - dp[i][0])
        ans += dp[i][1] * (dp[n][2] - dp[i][2])
        ans += dp[i][2] * (dp[n][1] - dp[i][1])
    print(ans)

if __name__ == "__main__":
    main()