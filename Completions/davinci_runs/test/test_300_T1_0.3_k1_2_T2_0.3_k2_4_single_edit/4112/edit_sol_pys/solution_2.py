
import sys

def main():
    n, k, x = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    dp = [[[0 for _ in range(x+1)] for _ in range(n+1)] for _ in range(n+1)] # dp[i][j][l] = i番目までの要素を使ってj番目までの要素を使い切り、l回以内に完成させるときの最大値
    for i in range(1, n+1):
        for j in range(1, n+1):
            for l in range(1, x+1):
                if i == j:
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j][l] + a[i-1]) # i番目の要素を使う
                else:
                    if i - j + 1 >= k:
                        dp[i][j][l] = max(dp[i][j][l], dp[i-1][j][l] + a[i-1]) # i番目の要素を使う
                    if l > 1:
                        dp[i][j][l] = max(dp[i][j][l], dp[i-1][i][l-1] + a[i-1]) # i番目の要素を使う
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j][l]) # i番目の要素を使わない
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
