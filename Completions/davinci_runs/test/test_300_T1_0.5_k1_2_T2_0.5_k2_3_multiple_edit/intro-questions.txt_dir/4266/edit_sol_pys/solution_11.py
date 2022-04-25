import sys

k, x = list(map(int, sys.stdin.readline().split()))

for i in range(x - k + 1, x + k):
    if i > -1000000 and i < 1000000:
        print(i, end=" ")
