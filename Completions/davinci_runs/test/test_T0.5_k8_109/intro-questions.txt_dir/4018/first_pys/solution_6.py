

def main():
    n, k = map(int, input().split())
    s = input()

    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = dp[i-1] + i

    for i in range(n, 0, -1):
        if dp[i] <= k:
            return dp[i]
    return -1

print(main())