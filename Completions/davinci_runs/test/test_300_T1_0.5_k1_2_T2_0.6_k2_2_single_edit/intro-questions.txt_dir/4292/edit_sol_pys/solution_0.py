# Python3

import sys

n, k = map(int, sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))

sorted_p = sorted(p)
print(sum(sorted_p[:k]))
