
import sys

def solve(a, n, m, rain, umbrellas, umbrellas_sorted):
    r = [0] * (a + 1)
    for l, ri in rain:
        r[l] += 1
        r[ri] -= 1
    for i in range(1, a + 1):
        r[i] += r[i - 1]
    dp = [0] * (a + 1)
    for i in range(1, a + 1):
        dp[i] = dp[i - 1] + r[i - 1]
    for i in range(1, a + 1):
        if i in umbrellas:
            dp[i] = min(dp[i], dp[i - 1] + umbrellas[i])
    for i in range(a - 1, -1, -1):
        dp[i] = min(dp[i], dp[i + 1])
    if dp[a] == sys.maxsize:
        return -1
    return dp[a]

def main():
    a, n, m = map(int, input().split())
    rain = [tuple(map(int, input().split())) for _ in range(n)]
    umbrellas = dict([tuple(map(int, input().split())) for _ in range(m)])
    umbrellas_sorted = sorted(umbrellas.keys())
    print(solve(a, n, m, rain, umbrellas, umbrellas_sorted))

if __name__ == "__main__":
    main()
