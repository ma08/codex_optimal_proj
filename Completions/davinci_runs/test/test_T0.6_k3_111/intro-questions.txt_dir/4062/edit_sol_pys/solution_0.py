import sys

a, b, c, d = map(int, sys.stdin.readline().split())
ans = (b - a + 1) * (d - c + 1)
print(ans)
