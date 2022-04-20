

def main():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*(m+1) for _ in range(n+1)]  # dp[i][j] = i行j列までの1の数
    dp[1][1] = 1
    for i in range(1, n+1):  # 初期化
        for j in range(1, m+1):  # 初期化
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    for i in range(1, n+1):  # 差分を取る
        for j in range(1, m+1):  # 差分を取る
            dp[i][j] -= dp[i-1][j-1]
    ans = 0
    for i in range(1, n+1):  # 回答を求める
        for j in range(1, m+1):  # 回答を求める
            if a[i-1][j-1] ^ k == 0:
                ans += dp[i][j]
    print(ans)

if __name__ == "__main__":
    main()
