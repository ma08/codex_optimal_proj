

def main():
    n, k = map(int, input().split())
    s = input()
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n + 1):
            dp[i][j] = dp[i][j - 1] + 1 if s[j - 1] == '1' else dp[i][j - 1]
    ans = 0
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            if dp[i][j] >= k:
                ans = max(ans, j - i)
    print(ans)

if __name__ == '__main__':
    main()
