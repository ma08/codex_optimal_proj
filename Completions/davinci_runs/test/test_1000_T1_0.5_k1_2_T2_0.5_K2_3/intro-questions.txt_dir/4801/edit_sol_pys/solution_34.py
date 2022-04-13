

from sys import stdin

N = int(stdin.readline())
A = [int(x) for x in stdin.readline().split()]

def lis(A):
    g = []
    for a in A:
        if not g or a > g[-1]:
        else:
            i = bisect.bisect(g, a)
            g[i] = a
            g.append(a)
    return g

g = lis(A)

print(len(g))
print(*g)
