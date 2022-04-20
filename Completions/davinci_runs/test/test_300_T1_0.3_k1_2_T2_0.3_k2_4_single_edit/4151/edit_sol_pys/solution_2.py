
def main():
    n = int(input())
    a = list(map(int, input().split()))

    # dp[i] = number of ways to renumber a[:i+1]
    dp = [1]
    for i in range(1, n):
        if a[i] == a[i - 1]:
            dp.append(dp[-1])
        else:
            dp.append((dp[-1] + dp[-2]) % MOD)

    print(dp[-1])


MOD = 998244353

if __name__ == '__main__':
    main()
