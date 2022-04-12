from sys import stdin

N = int(stdin.readline())
A = [int(x) for x in stdin.readline().split()]

def gis(A):
    gis = []
    for i in A:
        if not gis or i > gis[-1]:
            gis.append(i)
    return gis

gis = gis(A)

print(len(gis))
print(*gis)
