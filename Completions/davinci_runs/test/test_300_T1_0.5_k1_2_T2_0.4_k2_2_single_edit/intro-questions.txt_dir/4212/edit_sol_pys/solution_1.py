
def main():
    n, m, q = map(int, input().split())  # 入力
    abcd = [list(map(int, input().split())) for _ in range(q)]  # 入力
    abcd.sort(key=lambda x: (x[1], x[0]))  # ソート
    dp = [[0 for _ in range(m)] for _ in range(n+1)]  # 初期化

    for i in range(1, n+1):  # 初期化
        for j in range(m):  # 初期化
            dp[i][j] = dp[i-1][j]  # 初期化

    for a, b, c, d in abcd:  # 入力
        for j in range(c, m):  # 入力
            dp[b][j] = max(dp[b][j], dp[a][j-c] + d)  # 入力

    print(max(dp[n]))  # 出力

if __name__ == '__main__':
    main()  # 出力
