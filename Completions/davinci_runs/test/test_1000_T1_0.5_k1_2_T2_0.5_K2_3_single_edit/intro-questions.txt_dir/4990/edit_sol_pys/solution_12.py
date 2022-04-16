
import sys

a, b, c = map(int, sys.stdin.readline().split())
print(int(a / c) + (1 if a % c > 0 else 0))
