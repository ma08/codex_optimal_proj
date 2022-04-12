import sys

a, b = map(int, sys.stdin.readline().split())

if a == 1:
    print(b - a)
else:
    print(b - a - 1)
