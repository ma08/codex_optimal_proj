
import sys

x, k, d = map(int, sys.stdin.readline().rstrip().split())
if abs(x) < k * d:
    print(abs(x - (x // d) * d))
else:
    print(abs(x) - (k * d))
