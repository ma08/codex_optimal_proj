

def main():
    # Read input
    N, M = map(int, input().split())
    a = set(map(int, [input() for _ in range(M)]))

    # Initialize DP table
    dp = [0] * (N + 1)
    dp[0] = 1

    # Fill in DP table
    for i in range(1, N + 1):
        if i - 1 not in a:
            dp[i] += dp[i - 1]
        if i - 2 not in a:
            dp[i] += dp[i - 2]

    # Print answer
    print(dp[N] % 1000000007)

if __name__ == '__main__':
    main()