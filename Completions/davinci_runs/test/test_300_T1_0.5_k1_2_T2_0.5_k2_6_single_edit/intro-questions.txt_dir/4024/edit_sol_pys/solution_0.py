def main():
    n, k = map(int, input().split())
    s = input()
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if s[j:i] in s:
                dp[i] = max(dp[i], dp[j] + n - i + j)
    if dp[n] < k:
        print(-1)
    else:
        print(dp[n])



def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            ans += a[i]
    print(ans)


if __name__ == '__main__':
    main()
