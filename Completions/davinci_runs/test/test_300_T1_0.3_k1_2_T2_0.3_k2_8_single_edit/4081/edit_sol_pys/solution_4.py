

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a + [0]
    dp = [[0, 0] for _ in range(n + 1)]
    for i in range(1, n + 1):
        if a[i] > a[i - 1]:
            dp[i][0] = dp[i - 1][0] + 1 + dp[i - 1][1]
            dp[i][1] = dp[i - 1][1]
        else:
            dp[i][0] = dp[i - 1][0] + 1
            dp[i][1] = dp[i - 1][1] + 1
    print(max(dp[-1]) - 1)
    print(dp)

if __name__ == "__main__":
    main()
