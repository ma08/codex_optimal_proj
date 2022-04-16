from math import factorial

import sys

def main():
    n, k = sys.stdin.readline().split()
    n = int(n)
    k = int(k)
    print(factorial(n)/factorial(n-k)/factorial(k))

main()
