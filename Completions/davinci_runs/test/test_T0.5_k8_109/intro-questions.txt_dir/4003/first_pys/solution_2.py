

def main():
    n = int(input())
    a = list(map(int, input().split()))
    # print(n, a)

    # dp = [0] * n
    # for i in range(n):
    #     dp[i] = 1
    #     for j in range(0, i):
    #         if a[i] > a[j]:
    #             dp[i] = max(dp[i], dp[j] + 1)
    # print(dp)
    # print(max(dp))

    dp = [0] * n
    for i in range(n):
        dp[i] = 1
        for j in range(i - 1, -1, -1):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(dp)
    print(max(dp))

if __name__ == '__main__':
    main()