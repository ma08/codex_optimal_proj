

from sys import stdin

N = int(stdin.readline())
A = [int(x) for x in stdin.readline().split()]

def lis(A):
    g = []
    for a in A:
        if not g or a > g[-1]:
            g.append(a)
    return len(g)

print(lis(A))
