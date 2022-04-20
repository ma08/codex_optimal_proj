
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    print(dp[n][m])

if __name__ == '__main__':
    main()
