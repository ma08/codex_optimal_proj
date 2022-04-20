import sys


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

l = [0] * n

for i in range(n):
    l[a[i]-1] = i+1

for i in range(n):
    if i == n-1:
        print(l[i])
    else:
        sys.stdout.write(str(l[i])+' ')
