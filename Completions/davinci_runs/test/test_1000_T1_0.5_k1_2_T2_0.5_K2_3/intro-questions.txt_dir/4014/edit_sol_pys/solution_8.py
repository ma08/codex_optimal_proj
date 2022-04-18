def main():
    n = int(input())
    w = list(map(int, input().split()))

    dp = [0] * n
    dp[1] = abs(w[1] - w[0])
    for i in range(2, n):
        dp[i] = min(dp[i - 1] + abs(w[i] - w[i - 1]), dp[i - 2] + abs(w[i] - w[i - 2]))

    print(dp[-1])


if __name__ == "__main__":
    main()
