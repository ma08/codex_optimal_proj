

def main():
    n, k = map(int, input().split())
    s = input()
    if k > n:
        print(-1)
        return
    if n == k:
        print(n * (n + 1) // 2)
        return
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + i
    print(dp[k - 1] + (n - k) * k)

if __name__ == "__main__":
    main()