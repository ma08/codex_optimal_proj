
import sys

def solve(a, n, m, rain, umbrellas):
    umbrellas = sorted(umbrellas)
    r = [0] * (a + 2)
    for l, ri in rain:
        r[l] += 1
        r[ri + 1] -= 1
    for i in range(1, a + 1):
        r[i] += r[i - 1]
    dp = [sys.maxsize] * (a + 2)
    dp[0] = 0
    for i in range(1, a + 1):
        dp[i] = dp[i - 1] + r[i]
    for i in range(m):
        x, p = umbrellas[i]
        dp[x] = min(dp[x], dp[x - 1] + p)
    for i in range(a - 1, -1, -1):
        dp[i] = min(dp[i], dp[i + 1])
    if dp[a] == sys.maxsize:
        return -1
    return dp[a]

def main():
    a, n, m = map(int, input().split())
    rain = [tuple(map(int, input().split())) for _ in range(n)]
    umbrellas = [tuple(map(int, input().split())) for _ in range(m)]
    print(solve(a, n, m, rain, umbrellas))

if __name__ == "__main__":
    main()
