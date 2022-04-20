

def count_substr(s):
    dp = [0] * (len(s) + 1)
    for i in range(1, len(s) + 1):
        for j in range(i):
            if s[j:i] in s:
                dp[i] = max(dp[i], dp[j] + len(s) - i + j)
    return dp[len(s)]

def main():
    n, k = map(int, input().split())
    s = []
    for _ in range(n):
        s.append(input())
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if count_substr(s[i:j + 1]) >= k:
                ans = max(ans, j - i + 1)
    if ans == 0:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()
