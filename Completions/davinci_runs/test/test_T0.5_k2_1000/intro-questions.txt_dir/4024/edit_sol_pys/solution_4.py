
def main():
    n, k = map(int, input().split())
    s = input()
    dp = [0] * (n + 1)  # dp[i] = max(dp[j] + n - i + j) for j < i
    for i in range(1, n + 1):
        for j in range(i):
            if s[j:i] in s[:j]:
                dp[i] = max(dp[i], dp[j] + n - i + j)
    if dp[n] < k:
        print(-1)
    else:
        print(dp[n])

if __name__ == '__main__':
    main()
