

def main():
    n, k = [int(x) for x in input().split()]
    s = input()
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + i
    if dp[n] < k:
        print(-1)
    else:
        ans = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[j] - dp[i] >= k:
                    ans += j - i
                    break
        print(ans)

if __name__ == "__main__":
    main()