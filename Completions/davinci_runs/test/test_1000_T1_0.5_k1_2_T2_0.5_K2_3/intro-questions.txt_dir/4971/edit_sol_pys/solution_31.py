

from sys import stdin, stdout

def isCube(x):
    return round(x**(1/3))**3 == x

def buscar(m, n):
    maxi = 0
    for i in range(m, n + 1):
        for j in range(i, n + 1):
            if isCube(i) and isCube(j) and i + j <= m:
                if i + j > maxi:
                    maxi = i + j
    return maxi

stdout.write(str(buscar(int(stdin.readline()), int(stdin.readline()))))
