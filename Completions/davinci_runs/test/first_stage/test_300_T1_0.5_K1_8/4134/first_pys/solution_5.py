

def main():
    # read
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    # solve
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    dp2 = [[0] * (m+1) for _ in range(n+1)]
    dp2[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            dp2[i][j] = dp2[i-1][j] + dp2[i][j-1]

    ans = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            xor_sum = a[i-1][j-1] ^ k
            if xor_sum > k:
                continue
            ans += dp[i-1][j] * dp2[n][m-j+1] + dp[i][j-1] * dp2[n-i+1][m]

    print(ans)

if __name__ == "__main__":
    main()