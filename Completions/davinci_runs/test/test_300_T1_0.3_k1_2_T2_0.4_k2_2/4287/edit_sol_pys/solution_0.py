
import sys


def solve(a, n, m, rain, umbrellas, k):
    umbrellas = sorted(umbrellas)
    r = [0] * (k + 1)
    for l, ri in rain:
        r[l] += 1
        r[ri] -= 1
    for i in range(1, k + 1):
        r[i] += r[i - 1]
    dp = [0] * (k + 1)
    for i in range(1, k + 1):
        dp[i] = dp[i - 1] + r[i - 1]
    for i in range(m):
        x, p = umbrellas[i]
        dp[x] = min(dp[x], dp[x - 1] + p)
    for i in range(k - 1, -1, -1):
        dp[i] = min(dp[i], dp[i + 1])
    if dp[k] == sys.maxsize:
        return -1
    return dp[k]


def main():
    a, n, m = map(int, input().split())
    rain = [tuple(map(int, input().split())) for _ in range(n)]
    umbrellas = [tuple(map(int, input().split())) for _ in range(m)]
    k = max(map(lambda x: x[1], rain))
    print(solve(a, n, m, rain, umbrellas, k))


if __name__ == "__main__":
    main()
