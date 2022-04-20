
from sys import stdin

n, k = map(int, stdin.readline().split())
a = map(int, stdin.readline().split())

print(sorted(a)[k - 1] if k else -1)
