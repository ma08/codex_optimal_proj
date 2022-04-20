
from sys import stdin
n, k = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))

print(a[k - 1] if k else -1)
