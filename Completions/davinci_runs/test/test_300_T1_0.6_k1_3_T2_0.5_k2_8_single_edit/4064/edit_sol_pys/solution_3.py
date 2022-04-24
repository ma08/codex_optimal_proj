import sys


sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n, h, l, r = inl()
    a = inl()

ans = 0
for i in range(l, r + 1):
    ans = max(ans, dp[n - 1][i])

print(ans)
