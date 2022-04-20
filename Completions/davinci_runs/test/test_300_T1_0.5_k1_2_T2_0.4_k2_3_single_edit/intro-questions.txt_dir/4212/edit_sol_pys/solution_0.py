

def main():
    n, m, q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(q)]  # 質問のリスト
    abcd.sort(key=lambda x: (x[1], x[0]))  # 時間でソート
    dp = [[0 for _ in range(m)] for _ in range(n+1)]  # DPテーブル

    for i in range(1, n+1):  # 初期化
        for j in range(m):
            dp[i][j] = dp[i-1][j]

    for a, b, c, d in abcd:  # DP
        for j in range(c, m):  # 開始時間
            dp[b][j] = max(dp[b][j], dp[a][j-c] + d)  # 終了時間

    print(max(dp[n]))

if __name__ == '__main__':
    main()
