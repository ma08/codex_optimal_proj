
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort(reverse=True)
c = []

for i in range(n):
    c.append(a.pop(0))
    if a and a[0]*2 == c[-1]:
        c.append(a.pop(0))

print(' '.join(map(str, c)))
