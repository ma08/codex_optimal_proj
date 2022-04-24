def main():
    n, k = map(int, input().split())
    s = input()
    dp = [1] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i - 1, -1, -1):
            if s[j:i] in s[:j]:
                dp[i] = min(dp[i], dp[j] + 1)
                break
    print(dp[n])

if __name__ == '__main__':
    main()
