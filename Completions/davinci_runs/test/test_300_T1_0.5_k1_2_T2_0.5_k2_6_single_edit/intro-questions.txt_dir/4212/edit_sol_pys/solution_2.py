

def main():
    n, m, q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(q)]  # 問題を読み込む
    abcd.sort(key=lambda x: (x[1], x[0]))  # 問題をbでソート。bが同じならaでソート
    dp = [[0 for _ in range(m)] for _ in range(n+1)]  # dpテーブルを初期化

    for i in range(1, n+1):
        for j in range(m):
            dp[i][j] = dp[i-1][j]

    for a, b, c, d in abcd:  # 問題を順番に処理
        for j in range(c, m):
            dp[b][j] = max(dp[b][j], dp[a][j-c] + d)  # dp[b][j]に最大値を入れる

    print(max(dp[n]))

if __name__ == '__main__':
    main()
