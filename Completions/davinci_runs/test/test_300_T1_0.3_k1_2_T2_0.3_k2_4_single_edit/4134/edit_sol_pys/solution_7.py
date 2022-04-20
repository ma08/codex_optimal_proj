

def main():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*(m+1) for _ in range(n+1)]  # dp[i][j] = (1,1)から(i,j)までの距離の組み合わせ
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]  # 左から来る組み合わせと上から来る組み合わせを足す
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] -= dp[i-1][j-1]  # 左上から来る組み合わせを引く
    ans = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1][j-1] ^ k == 0:
                ans += dp[i][j]
    print(ans)

if __name__ == "__main__":
    main()
