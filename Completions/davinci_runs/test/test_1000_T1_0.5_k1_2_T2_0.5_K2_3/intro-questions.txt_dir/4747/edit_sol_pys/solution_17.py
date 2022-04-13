

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())

    print(calculate(n,k))

def calculate(n,k):
    if k == 1:
        return (n+1)//2
    else:
        return (n+1)//2 + ((n-1)/n)*(k-1)*calculate(n-1,k-1)

main()
