

def main():
    n = int(input())
    candies = [int(x) for x in input().split()]

    dp = [0] * (n + 1)

    dp[1] = candies[0]
    for j in range(2, n + 1):
        dp[j] = max(dp[j - 1], dp[j - 2] + candies[j - 1])

    print(dp[n])

if __name__ == '__main__':
    main()
