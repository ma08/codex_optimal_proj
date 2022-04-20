

def solve(n, m, p):
    dp = [0] * (n + 1)  # dp[i] = # of times i appears

    for i in range(n):
        if p[i] == m:
            dp[i + 1] += 1

    return sum(dp)


if __name__ == "__main__":
    n, m = [int(i) for i in input().split()]
    p = [int(i) for i in input().split()]

    print(solve(n, m, p))
