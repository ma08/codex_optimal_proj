

import sys
from math import factorial

def nCr(n,r):
    return factorial(n) / factorial(r) / factorial(n-r)

def p(n):
    return 1 - (nCr(n,1) + nCr(n,2)) / nCr(n,n) # probability of no collision

def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    print(p(n))

if __name__ == "__main__":
    main('file')
