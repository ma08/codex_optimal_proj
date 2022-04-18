def max_three_block_palindrome(arr):
    n = len(arr)

    # Create a 2d array where dp[i][j] is the length of the longest
    # three blocks palindrome that includes a_i and a_j.
    dp = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            # If i is greater than j, then dp[i][j] is 0.
            if i > j:
                dp[i][j] = 0
            # If i is equal to j, then dp[i][j] is 1.
            elif i == j:
                dp[i][j] = 1
            # If a_i is equal to a_j, then dp[i][j] is 2.
            elif arr[i] == arr[j]:
                dp[i][j] = 2
            # If a_i is not equal to a_j, then dp[i][j] is the maximum
            # of dp[i+1][j], dp[i][j-1], dp[i+1][j-1] + 2.
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1], dp[i+1][j-1] + 2)

    return dp[0][n-1]


def main():
    # Read the number of test cases.
    t = int(input())

    # Iterate over the test cases.
    for i in range(t):
        # Read the array length.
        n = int(input())
        # Read the array.
        arr = list(map(int, input().split()))

        # Print the result.
        print(max_three_block_palindrome(arr))


if __name__ == '__main__':
    main()