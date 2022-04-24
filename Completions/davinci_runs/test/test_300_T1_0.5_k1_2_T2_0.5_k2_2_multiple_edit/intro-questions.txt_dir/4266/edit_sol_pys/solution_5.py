import sys

k, x = map(int, sys.stdin.readline().split())

print(" ".join(map(str, range(x - k + 1, x + k))))
