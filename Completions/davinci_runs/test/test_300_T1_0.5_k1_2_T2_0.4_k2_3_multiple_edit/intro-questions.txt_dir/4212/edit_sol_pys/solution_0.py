

def main():
    n, m, q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(q)]  # 問題を入力
    abcd.sort(key=lambda x: (x[1], x[0]))  # 問題をbでソート(bが同じならaでソート)
    dp = [[0 for _ in range(m)] for _ in range(n+1)]

    for i in range(1, n+1):  # dpテーブルの初期化
        for j in range(m):
            dp[i][j] = dp[i-1][j]

    for a, b, c, d in abcd:  # dpテーブルの更新
        for j in range(c, m):
            dp[b][j] = max(dp[b][j], dp[a][j-c] + d)

    print(max(dp[n]))

if __name__ == '__main__':
    main()
