

from sys import stdin, stdout

def isCube(x):
    return round(x**(1/3))**3 == x and x != 0

def bus(m):
    _max = 0
    for i in range(1, m + 1):
        for j in range(i, m + 1):
            if isCube(i) and isCube(j):
                if i + j <= m:
                    if i + j > _max:
                        _max = i + j
    return _max

stdout.write(str(bus(int(stdin.readline()))))
