

def solve(n, m, p):
    dp = [0] * (n + 1)

    for i in range(n):
        for j in range(i + 1, n + 1):
            if p[j - 1] == m:
                dp[j] += 1

    return sum(dp)


if __name__ == "__main__":
    n, m = [int(i) for i in input().split()]
    p = [int(i) for i in input().split()]

    print(solve(n, m, p))