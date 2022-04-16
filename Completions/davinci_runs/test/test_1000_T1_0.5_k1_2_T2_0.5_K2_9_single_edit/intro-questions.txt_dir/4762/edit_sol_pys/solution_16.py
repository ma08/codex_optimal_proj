
import sys
from math import factorial

def nCr(n,r):
    return factorial(n) / factorial(r) / factorial(n-r)

def p(n):
    return 1 - (nCr(n,1) + nCr(n,2)) / nCr(n,n)

def main(pname):
    sys.stdin = open(pname + '.in', 'r') #input file
    sys.stdout = open(pname + '.out', 'w') #output file

    n = int(input())
    print(p(n))

if __name__ == "__main__":
    main('gift1')
