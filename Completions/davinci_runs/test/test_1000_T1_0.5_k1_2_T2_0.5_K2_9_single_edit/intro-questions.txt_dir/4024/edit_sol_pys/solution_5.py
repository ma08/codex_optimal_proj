
def main():
    n, k = map(int, input().split())
    s = input()
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i - 1, -1, -1):
            if s[j:i] == s[i:2 * i - j]:
                dp[i] = max(dp[i], dp[j] + i - j)
    if dp[n] < k:
        print(-1)
    else:
        print(dp[n])

if __name__ == '__main__':
    main()
