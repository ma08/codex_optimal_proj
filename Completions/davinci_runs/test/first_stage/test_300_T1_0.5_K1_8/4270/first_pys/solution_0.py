

import sys

N = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))
values.sort()

for i in range(N - 1):
    values.append((values[0] + values[1]) / 2)
    values.pop(0)
    values.pop(0)
    values.sort()

print(values[0])