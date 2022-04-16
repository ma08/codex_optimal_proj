

def main():
    n, k = map(int, input().split())
    s = input()
    dp = [0] * (n + 1)
        if dp[i] >= k:
            print(i)
            exit()
    for i in range(1, n + 1):
        for j in range(i):
            if s[j:i] in s:
                dp[i] = max(dp[i], dp[j] + n - i + j)
    print(-1)

if __name__ == '__main__':
    main()
