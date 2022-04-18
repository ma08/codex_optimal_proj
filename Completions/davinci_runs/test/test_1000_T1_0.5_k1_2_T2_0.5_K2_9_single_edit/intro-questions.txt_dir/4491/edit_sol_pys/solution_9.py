

def main():
    n = int(input())
    candies_1 = [int(x) for x in input().split()][:n]
    candies_2 = [int(x) for x in input().split()][:n]

    dp = [[0] * (n+1) for _ in range(2)]

    dp[0][1] = candies_1[0]
    dp[1][1] = candies_2[0]
    for j in range(2, n+1):
        dp[0][j] = max(dp[0][j-1], dp[1][j-1]) + candies_1[j-1]
        dp[1][j] = max(dp[0][j-1], dp[1][j-1]) + candies_2[j-1]

    print(max(dp[0][n], dp[1][n]))

if __name__ == '__main__':
    main()
