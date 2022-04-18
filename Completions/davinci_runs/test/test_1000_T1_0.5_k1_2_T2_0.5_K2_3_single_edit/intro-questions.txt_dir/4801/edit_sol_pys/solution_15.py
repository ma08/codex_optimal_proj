

from sys import stdin

N = int(stdin.readline())
A = [int(x) for x in stdin.readline().split()]

def gis(A):
    gis = []
    for num in A:
        if not gis or num > gis[-1]:
            gis.append(num)
    return gis

gis = gis(A)

print(len(gis))
print(*gis)
