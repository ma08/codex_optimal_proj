import sys
n, m = map(int, input().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a.sort()
b.sort()
for i in range(m):
    print(a[i] + b[m - i - 1])
