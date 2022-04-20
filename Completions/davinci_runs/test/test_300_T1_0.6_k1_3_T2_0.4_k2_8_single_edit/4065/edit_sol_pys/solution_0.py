
def getMaxContest(a):
    n = len(a)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if a[i] <= 2 * a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def main():
    a = list(map(int, input().split()))
    print(getMaxContest(a))

if __name__ == '__main__':
    main()
