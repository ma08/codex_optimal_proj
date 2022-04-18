import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inm = lambda: map(int, sys.stdin.readline().split())
inl = lambda: list(inm())
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


N = int(input())

days = [0 for i in range(365)]

for i in range(N):
    start, end = map(int, input().split())
    for j in range(start - 1, end):
        days[j] += 1



exit()

# TLE

N, M = inm()


def solve(i, j, k):
    if i == 0:
        return 1
    if j == 0:
        return 0
    if k == 0:
        return 0
    if i < 0:
        return 0
    if dp[i][j][k] != -1:
        return dp[i][j][k]
    a = solve(i - A[j], j - 1, k)
    b = solve(i, j - 1, k)
    c = solve(i - A[j], j - 1, k - 1)
    return dp[i][j][k] = a + b + c


A = [0] + inl()
dp = [[[-1 for _ in range(M + 1)] for _ in range(N + 1)] for _ in range(N + 1)]
print(solve(N, N, M))
print(sum(days))
