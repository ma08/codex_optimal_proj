
def main():
    # Read input
    n, m = map(int, input().split())
    a = set(map(int, [input() for _ in range(m)]))

    # Initialize DP table
    dp = [0] * (n + 1)
    dp[0] = 1

    # Fill in DP table
    for i in range(1, n + 1):
        if i - 1 not in a:
            dp[i] += dp[i - 1]
        if i - 2 not in a:
            dp[i] += dp[i - 2]

    # Print answer
    print(dp[n] % 1000000007)

if __name__ == '__main__':
    main()
