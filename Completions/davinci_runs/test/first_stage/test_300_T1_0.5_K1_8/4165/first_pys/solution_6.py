

import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

if max(L) < sum(L) - max(L):
    print("Yes")
else:
    print("No")