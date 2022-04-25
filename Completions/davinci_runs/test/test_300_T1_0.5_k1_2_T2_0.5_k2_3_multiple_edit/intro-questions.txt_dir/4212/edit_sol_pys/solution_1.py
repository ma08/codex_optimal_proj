

def main():
    n, m, q = map(int, input().split())  # n: 人数, m: 質問数, q: クエリ数
    abcd = [list(map(int, input().split())) for _ in range(q)]  # abcd[i]: i番目のクエリ
    abcd.sort(key=lambda x: (x[1], x[0]))  # bでソートしてaで昇順ソート
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]  # dp[i][j]: i人目までの質問をj個聞いたときの最大値
    # dpテーブルの初期化

    for i in range(1, n+1):
        for j in range(m+1):
            dp[i][j] = dp[i-1][j]

    for a, b, c, d in abcd:  # a: 質問をする人数, b: 回答する人数, c: 回答する質問数, d: 回答するときの報酬
        for j in range(c, m+1):
            dp[b][j] = max(dp[b][j], dp[a][j-c] + d)

    print(max(dp[n][:-1]))  # dp[n][m]は存在しないので、dp[n]の最大値を出力

if __name__ == '__main__':
    main()
