
import sys

def main():
    n, k, x = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    dp = [[[0 for _ in range(x+1)] for _ in range(n+1)] for _ in range(n+1)] # dp[i][j][l] = i번째 수까지 봤을 때, j번째 수를 선택했을 때, l번째 선택했을 때 최대값
    for i in range(1, n+1):
        for j in range(1, n+1):
            for l in range(1, x+1):
                if i == j:
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j][l] + a[i-1])
                else:
                    if i - j + 1 >= k:
                        dp[i][j][l] = max(dp[i][j][l], dp[i-1][j][l] + a[i-1])
                    if l > 1:
                        dp[i][j][l] = max(dp[i][j][l], dp[i-1][i][l-1] + a[i-1])
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j][l])
    ans = 0
    for i in range(1, n+1):
        for j in range(1, x+1):
            ans = max(ans, dp[n][i][j])
    if ans == 0:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()
