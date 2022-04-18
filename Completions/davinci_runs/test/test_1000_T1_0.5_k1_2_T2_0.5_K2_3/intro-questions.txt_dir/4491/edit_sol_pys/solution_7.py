

def main():
    n = int(input())
    n_candies = [int(x) for x in input().split()]

    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][1] = n_candies[i-1]
        dp[i][0] = dp[i-1][0]
    for i in range(1, n+1):
        for j in range(2, n+1):
            if i < j:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-j][j]) + n_candies[i-1]

    print(dp[n][n])

if __name__ == '__main__':
    main()
