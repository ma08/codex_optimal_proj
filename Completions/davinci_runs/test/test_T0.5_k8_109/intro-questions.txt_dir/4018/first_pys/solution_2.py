


def main():
    """
    We can use dynamic programming to solve this problem.
    Let dp[i][j] be the minimum cost to obtain a set of size j using the first i characters of the string.
    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + n-i+1)
    """
    n, k = [int(x) for x in input().split()]
    s = input()
    dp = [[0]*(k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][1] = n-i+1
    for i in range(1, n+1):
        for j in range(2, k+1):
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + n-i+1)
    if dp[n][k] > 10**12:
        print(-1)
    else:
        print(dp[n][k])


if __name__ == "__main__":
    main()