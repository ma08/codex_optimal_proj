import sys

k, x = map(int, sys.stdin.readline().split())

for i in range(max(x - k + 1, -1 * 10 ** 6), min(x + k, 10 ** 6) + 1):
    print(i, end=' ')
