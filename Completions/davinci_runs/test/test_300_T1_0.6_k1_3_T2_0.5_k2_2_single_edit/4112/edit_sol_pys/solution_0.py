import sys


def main():
    n, k, x = map(int, input().split())
    arr = list(map(int, input().split()))

    if k > x:
        print(-1)
        return

    # For each index i, dp[i] is the max sum of beauty values of pictures that
    # can be posted from index i to the end of the array
    dp = [0] * (n+1)
    dp[-1] = 0
    for i in range(n-1, -1, -1):
        dp[i] = max(dp[i+1], dp[max(0, i+k)] + arr[i])

print(dp[0])
