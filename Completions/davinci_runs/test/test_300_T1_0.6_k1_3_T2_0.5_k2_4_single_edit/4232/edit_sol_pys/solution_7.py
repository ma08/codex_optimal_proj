from sys import stdin
from bisect import bisect_left
n, k = map(int, stdin.readline().split())
a = sorted(map(int, stdin.readline().split()))

print(a[k - 1] if k else -1)
