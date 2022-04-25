import sys

k, x = map(int, sys.stdin.readline().split())

for i in range(k):
    print(x - k + 1 + i, end=' ')
