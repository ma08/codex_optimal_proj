from sys import stdin
n, k = map(int, stdin.readline().split())
a = map(int, stdin.readline().split())

print(a[k - 1] if k <= n else -1)
