

def main():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*(m+1) for _ in range(n+1)]  # dp[i][j] = (1, 1)から(i, j)までの経路数
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]  # (i, j)に移動する経路は(i-1, j)からの移動経路と(i, j-1)からの移動経路の和
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] -= dp[i-1][j-1]  # (i-1, j-1)からの移動経路は2回数えてしまっているので引いておく
    ans = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1][j-1] ^ k == 0:
                ans += dp[i][j]
    print(ans)

if __name__ == "__main__":
    main()
