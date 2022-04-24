
import sys

n, a, b = map(int, sys.stdin.readline().split())

if a < b:
    print(min(a, n - b))
else:
    print(min(n - a, b))
