import sys

n = int(sys.stdin.readline())
a = [int(i) for i in sys.stdin.readline().split()]

for i in range(n):
    print(a[i], end=' ')
