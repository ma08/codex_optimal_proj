
import sys

k, x = list(map(int, sys.stdin.readline().split()))

for i in range(1, k + 1):
    print(x - k + 1 + i, end=" ")
