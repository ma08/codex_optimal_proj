
def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(1, n):
        if len(set(s[:i]) & set(s[i:])) > 0:
            ans = i
    print(ans)

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    print(n - dp[n][m])


if __name__ == '__main__':
    main()
