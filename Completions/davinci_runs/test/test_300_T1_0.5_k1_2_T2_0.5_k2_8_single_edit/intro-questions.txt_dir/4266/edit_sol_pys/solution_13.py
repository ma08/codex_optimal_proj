import sys

k, x = list(map(int, sys.stdin.readline().split()))

if k == 1:
    print(x)
else:
    for i in range(k):
        print(x - k + 1 + i, end=" ")
