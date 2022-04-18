

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())

    print(calculate(n,m))

def calculate(n,m):
    if m == 1:
        return (n+1)//2.0
    else:
        return (n+1)//2.0 + (1.0 - 1.0/n)*(m-1)*calculate(n,m-1)

main()
