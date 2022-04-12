

from sys import stdin, stdout

def isCube(x):
    return round(x**(1/3))**3 == x

def busca(m):
    maximo = 0
    for i in range(1, m + 1):
        for j in range(i, m + 1):
            if isCube(i) and isCube(j):
                if i + j <= m:
                    if i + j > maximo:
                        maximo = i + j
    return maximo

stdout.write(str(busca(int(stdin.readline()))))
