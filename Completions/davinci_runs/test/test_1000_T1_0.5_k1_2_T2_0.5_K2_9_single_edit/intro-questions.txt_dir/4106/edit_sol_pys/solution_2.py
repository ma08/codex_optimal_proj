

from collections import defaultdict

def solve(n, a, b, c):
    dp = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: -1)))
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dp[i][j][k] == -1:
                    continue
                dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])
                dp[i][j+1][k] = max(dp[i][j+1][k], dp[i][j][k])
                dp[i][j][k+1] = max(dp[i][j][k+1], dp[i][j][k])
                dp[i+1][j+1][k] = max(dp[i+1][j+1][k], dp[i][j][k]+a[i])
                dp[i+1][j][k+1] = max(dp[i+1][j][k+1], dp[i][j][k]+b[i])
                dp[i][j+1][k+1] = max(dp[i][j+1][k+1], dp[i][j][k]+c[i])
    return max(dp[n][n][n], 0)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(solve(n, a, b, c))

if __name__ == "__main__":
    main()
