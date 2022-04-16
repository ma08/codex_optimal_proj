

import sys

N = int(sys.stdin.readline())

for a in range(100, N + 1):
    if len(set(list(str(a)))) == 1:
        print(a)
        break
