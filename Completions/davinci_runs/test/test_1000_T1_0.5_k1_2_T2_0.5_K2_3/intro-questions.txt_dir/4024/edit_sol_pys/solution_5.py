

def main():
    n, k = map(int, input().split())
    print(s)
    s = input()
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i + 1):
            if s[j:i] in s[i:n]:
    print(dp)
                dp[i] = max(dp[i], dp[j] + n - i + j + 1)
    if dp[n] < k:
        print(-1)
    else:
        print(dp[n])

if __name__ == '__main__':
    main()
