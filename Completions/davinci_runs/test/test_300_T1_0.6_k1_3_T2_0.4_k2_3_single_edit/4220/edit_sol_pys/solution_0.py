

import sys

n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().rstrip()
    k = int(sys.stdin.readline())
    if k > len(s):
        print(s)
    else:
        print(s[:k] + '...')
