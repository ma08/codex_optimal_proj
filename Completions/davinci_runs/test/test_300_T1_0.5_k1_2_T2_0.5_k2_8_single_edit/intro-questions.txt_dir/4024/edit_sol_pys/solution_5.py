

def main():
    n, k = map(int, input().split())
    s = input()
    dp = [0] * (n)
    for i in range(1, n):
        for j in range(i):
            if s[j:i] in s:
                dp[i] = max(dp[i], dp[j] + n - i + j)
    if dp[-1] < k:
        print(-1)
    else:
        print(dp[-1])

if __name__ == '__main__':
    main()
