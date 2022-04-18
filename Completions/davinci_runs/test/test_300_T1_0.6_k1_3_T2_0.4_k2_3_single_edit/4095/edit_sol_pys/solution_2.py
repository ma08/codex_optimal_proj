

def solve(n, m, p, a):
    dp = [0] * (n)

    for i in range(n):
        for j in range(i + 1, n):
            if p[j] == m:
                dp[j] = dp[j - 1] + a[j]

    return sum(dp)


if __name__ == "__main__":
    n, m = [int(i) for i in input().split()]
    p = [int(i) for i in input().split()]

    a = [int(i) for i in input().split()]

    print(solve(n, m, p, a))
