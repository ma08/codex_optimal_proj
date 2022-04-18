

import sys

N = int(sys.stdin.readline())

for i in range(N, 1000):
    if len(set(list(str(i)))) == 1:
        print(i)
        break
