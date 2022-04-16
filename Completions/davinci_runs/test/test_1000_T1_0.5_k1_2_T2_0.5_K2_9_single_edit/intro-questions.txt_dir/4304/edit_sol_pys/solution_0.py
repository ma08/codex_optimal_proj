
import sys

a, b = map(int, sys.stdin.readline().strip().split())

if a == 1 or b == 1:
    print(a + b - 1)
else:
    print(a + b - 2)
