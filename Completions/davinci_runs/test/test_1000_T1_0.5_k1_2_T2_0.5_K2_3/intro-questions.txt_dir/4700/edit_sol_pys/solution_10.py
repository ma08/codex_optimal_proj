
import sys
n,m = [int(i) for i in input().split()]
h = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

for i in range(m):
    if h[a[i]-1] > h[b[i]-1]:
        print(a[i])
    else:
        print(b[i])
