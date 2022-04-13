import sys

def rearrange(t, n):
    t = sorted(t)
    if n%2 == 0:
        t1 = t[:n//2]
        t2 = t[n//2:]
    else:
        t1 = t[:n//2]
        t2 = t[n//2+1:]
    t1.reverse()
    t1 = t1 + t2
    return t1
t = int(input())
n = [int(x) for x in input().split()]
print(*rearrange(n, t))
