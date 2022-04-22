import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

a.sort()

print(a[0]*a[n-1])
