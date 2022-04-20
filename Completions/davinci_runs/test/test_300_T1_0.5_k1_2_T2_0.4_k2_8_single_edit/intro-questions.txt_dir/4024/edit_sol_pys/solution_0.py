

def main():
    n, k = map(int, input().split())
    s = input()
    dp = [0] * (n + 1)
    for i in range(n):
        for j in range(i + 1):
            if s[j:i + 1] in s:
                dp[i + 1] = max(dp[i + 1], dp[j] + n - i + j)
    if dp[n] < k:
        print(-1)
    else:
        print(dp[n])

if __name__ == '__main__':
    main()
