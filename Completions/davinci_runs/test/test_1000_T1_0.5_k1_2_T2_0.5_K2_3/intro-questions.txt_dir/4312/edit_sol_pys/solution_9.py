

import sys

a, b, c, d = map(int, sys.stdin.readline().split())

if a > c:
    print("Yes")
elif a < c:
    print("No")
else:
    if b > d:
        print("Yes")
    else:
        print("No")
