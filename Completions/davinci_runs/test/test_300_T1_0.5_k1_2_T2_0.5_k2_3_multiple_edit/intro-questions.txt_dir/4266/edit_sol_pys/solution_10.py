import sys

a, b = list(map(int, sys.stdin.readline().split()))

for i in range(a, b + 1):
    print(i, end=" ")
