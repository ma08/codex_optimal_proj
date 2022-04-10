


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # dp[i][j] = number of pairs of indices (l, r) where l <= i and r <= j and median of a[l], a[l+1], ..., a[r] is exactly m
    dp = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i, n):
            if i == j:
                if a[i] == m:
                    dp[i][j] = 1
            else:
                if a[i] == m or a[j] == m:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
    print(dp[0][n-1])


if __name__ == "__main__":
    main()