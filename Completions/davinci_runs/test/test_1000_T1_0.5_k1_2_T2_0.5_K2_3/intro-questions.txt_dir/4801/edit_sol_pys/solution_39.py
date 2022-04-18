

from sys import stdin

N = int(stdin.readline())
A = [int(x) for x in stdin.readline().split()]

def gis(a):
    g = []
    for i in A:
        if not g or i > g[-1]:
            g.append(i)
    return g

g = gis(A)

print(len(g))
print(*g)
