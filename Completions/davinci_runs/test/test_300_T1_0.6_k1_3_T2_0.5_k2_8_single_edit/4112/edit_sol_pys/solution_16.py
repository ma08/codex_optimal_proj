

def get_max_beauty(n, k, x, arr):
    if k > x:
        return -1

    # For each index i, dp[i] is the max sum of beauty values of pictures that
    # can be posted from index i to the end of the array
    dp = [0] * (n+1)
    dp[-1] = 0
    for i in range(n-1, -1, -1):
        dp[i] = max(dp[i+1], dp[max(0, i+k)] + arr[i])

    return dp[0]

if __name__ == "__main__":
    n, k, x = map(int, input().split())
    arr = list(map(int, input().split()))
    print(get_max_beauty(n, k, x, arr))
