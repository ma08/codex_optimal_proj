
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

a.sort()

for i in range(n):
    print(a[i], end=' ')
