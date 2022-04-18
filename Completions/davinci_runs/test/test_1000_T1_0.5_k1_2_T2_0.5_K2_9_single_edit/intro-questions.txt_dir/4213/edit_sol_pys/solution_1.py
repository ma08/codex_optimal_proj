
import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

a.sort()

print(a[n-1] - a[0])
