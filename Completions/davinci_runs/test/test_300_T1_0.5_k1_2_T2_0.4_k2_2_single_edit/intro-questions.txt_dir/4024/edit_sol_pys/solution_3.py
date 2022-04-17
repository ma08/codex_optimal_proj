

def main():
    n, k = map(int, input().split())
    s = input()
    s_set = set()
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if s[j:i] in s_set:
        s_set.add(s[i])
                dp[i] = max(dp[i], dp[j] + n - i + j)
    if dp[n] < k:
        print(-1)
    else:
        print(dp[n])

if __name__ == '__main__':
    main()
