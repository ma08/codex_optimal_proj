
import sys

def solve(a, n, m, rain, umbrellas):
    umbrellas = sorted(umbrellas)
    r = [0] * (a + 1) # r stores the number of raindrops that fall on each street
    for l, ri in rain:
        r[l] += 1
        r[ri] -= 1
    for i in range(1, a + 1):
        r[i] += r[i - 1]
    dp = [0] * (a + 1) # dp stores the minimum cost of reaching the ith street
    for i in range(1, a + 1):
        dp[i] = dp[i - 1] + r[i - 1] # the cost of reaching the ith street is the cost of reaching the (i - 1)th street plus the number of raindrops that fall on the ith street
    for i in range(m):
        x, p = umbrellas[i]
        dp[x] = min(dp[x], dp[x - 1] + p) # the cost of reaching the xth street is the minimum of the cost of reaching the xth street without buying an umbrella and the cost of reaching the (x - 1)th street plus the price of the umbrella
    for i in range(a - 1, -1, -1):
        dp[i] = min(dp[i], dp[i + 1]) # the cost of reaching the ith street is the minimum of the cost of reaching the ith street and the cost of reaching the (i + 1)th street
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
