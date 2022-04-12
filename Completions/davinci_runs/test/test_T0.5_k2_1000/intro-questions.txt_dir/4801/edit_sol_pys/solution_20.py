

from sys import stdin

N = int(stdin.readline())
A = [int(x) for x in stdin.readline().split()]

def gis(a):
    g = []
    for x in a:
        if not g or x > g[-1]:
            g.append(x)
    return g

g = gis(A)

print(len(g))
print(*g)
