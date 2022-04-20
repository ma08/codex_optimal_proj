

def main():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*(m+1) for _ in range(n+1)]  # dp[i][j] := (i, j) で終わる数列の個数
    dp[1][1] = 1  # (1, 1) で終わる数列の個数は 1
    for i in range(1, n+1):  # 各マスについて
        for j in range(1, m+1):  # 各マスについて
            dp[i][j] = dp[i-1][j] + dp[i][j-1]  # (i, j) で終わる数列の個数は (i-1, j) で終わる数列の個数と (i, j-1) で終わる数列の個数の和
    for i in range(1, n+1):  # 各マスについて
        for j in range(1, m+1):  # 各マスについて
            dp[i][j] -= dp[i-1][j-1]  # (i, j) で終わる数列の個数は (i-1, j-1) で終わる数列の個数を引く
    ans = 0
    for i in range(1, n+1):  # 各マスについて
        for j in range(1, m+1):  # 各マスについて
            if a[i-1][j-1] ^ k == 0:  # a[i-1][j-1] と k の XOR が 0 なら
                ans += dp[i][j]  # 答えに dp[i][j] を足す
    print(ans)

if __name__ == "__main__":
    main()
