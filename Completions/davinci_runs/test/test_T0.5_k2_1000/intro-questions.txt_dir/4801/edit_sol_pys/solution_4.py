

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    dp = [0] * n
    dp[0] = a[0]
    for i in range(1, n)
        dp[i] = a[i]
        for j in range(i):
            if a[i] > a[j] and dp[i] < dp[j] + a[i]:
                dp[i] = dp[j] + a[i]
    print(max(dp))

if __name__ == "__main__":
    main()
