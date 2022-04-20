

def main():
    # Read input and convert to int
    N, M = map(int, input().split()) 
    a = set(map(int, [input() for _ in range(M)])) 

    # Initialize DP table with 0
    dp = [0] * (N + 1)
    dp[0] = 1

    # Fill in DP table

    for i in range(1, N + 1):
        if i - 1 not in a:
        # If i - 1 not in a, add dp[i - 1] to dp[i]
            dp[i] += dp[i - 1]
        if i - 2 not in a:
        # If i - 2 not in a, add dp[i - 2] to dp[i]
            dp[i] += dp[i - 2]

    # Print answer
    print(dp[N] % 1000000007)

if __name__ == '__main__':
    main()
