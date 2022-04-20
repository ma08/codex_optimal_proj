

import sys

k, x = map(int, sys.stdin.readline().split())

for i in range(max(x - k + 1, -1000000), min(x + k, 1000000) + 1): # k개의 수 출력
    print(i, end=' ')
