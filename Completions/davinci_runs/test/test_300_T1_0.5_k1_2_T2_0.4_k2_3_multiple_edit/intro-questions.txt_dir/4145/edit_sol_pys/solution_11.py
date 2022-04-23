def main():
    # read input
    n = int(input())

    # initialize
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2

    # calculate
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007

    # output
    print(dp[n])

if __name__ == '__main__':
    main()
