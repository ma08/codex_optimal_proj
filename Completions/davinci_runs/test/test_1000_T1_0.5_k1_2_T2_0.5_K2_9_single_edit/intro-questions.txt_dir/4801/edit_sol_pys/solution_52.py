
from sys import stdin

N = int(stdin.readline())

A = [int(x) for x in stdin.readline().split()]

def gis(A):
    g = []
    for a in A:
        if not g or a > g[-1]:
            g.append(a)
    return g


g = gis(A)

print(len(g))
print(*g)
