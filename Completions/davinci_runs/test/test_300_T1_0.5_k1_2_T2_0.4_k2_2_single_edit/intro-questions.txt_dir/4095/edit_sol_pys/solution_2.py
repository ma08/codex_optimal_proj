
import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    print(solve(n, m, p) % (10**9+7))

def solve(n, m, p):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m+1):
            if j - p[i] >= 0:
                dp[i+1][j] = dp[i][j] + dp[i][j-p[i]]
            else:
                dp[i+1][j] = dp[i][j]
    return dp[n][m]

if __name__ == "__main__":
    main()
