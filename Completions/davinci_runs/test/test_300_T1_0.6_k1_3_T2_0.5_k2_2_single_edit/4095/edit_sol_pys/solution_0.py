import sys



def solve(n, m, p):
    dp = [0] * (n + 1)

    for i in range(n):
        for j in range(i + 1, n + 1):
            if p[j - 1] == m:
    sys.setrecursionlimit(10 ** 7)

                dp[j] += 1

    return sum(dp)


if __name__ == "__main__":
    n, m = map(int, input().split())
    p = list(map(int, input().split()))

    print(solve(n, m, p))
