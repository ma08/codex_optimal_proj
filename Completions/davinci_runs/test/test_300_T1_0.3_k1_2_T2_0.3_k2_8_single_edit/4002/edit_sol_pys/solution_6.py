

def main():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(n)]
    dp = [[0] * (k + 1) for _ in range(m + 1)]
    for i in range(n):  # 行
        for j in range(m):  # 列
            for x in range(k):  # 前i行j列での余り
                dp[j + 1][(x + a[i][j]) % k] = max(dp[j + 1][(x + a[i][j]) % k], dp[j][x] + a[i][j])
    print(dp[m][0])  # 全ての行を使ったときの余り0

main()
