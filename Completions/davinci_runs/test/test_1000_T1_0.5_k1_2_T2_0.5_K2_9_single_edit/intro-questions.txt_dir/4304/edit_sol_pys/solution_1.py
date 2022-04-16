
import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
if a == 0:
    if b == 0:
        print(0)
    else:
        print(b - a)
else:
    print(b - a - 1)
