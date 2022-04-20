
import sys

x, k = list(map(int, sys.stdin.readline().split()))

for i in range(x - k + 1, x + k):
    print(i, end=" ")
