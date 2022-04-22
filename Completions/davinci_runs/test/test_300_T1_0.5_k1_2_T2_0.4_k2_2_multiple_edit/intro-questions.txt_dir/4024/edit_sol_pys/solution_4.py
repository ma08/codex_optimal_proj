

def main():
    n, k = map(int, input().split())
    s = input()
    dp = [0] * n
    for i in range(1, n):
        for j in range(i - 1):
            if s[j:i] in s[i:]:
                dp[i] = max(dp[i], dp[j] + i - j)
    if dp[n - 1] < k:
        print(-1)
    else:
        print(dp[n - 1])

if __name__ == '__main__':
    main()
