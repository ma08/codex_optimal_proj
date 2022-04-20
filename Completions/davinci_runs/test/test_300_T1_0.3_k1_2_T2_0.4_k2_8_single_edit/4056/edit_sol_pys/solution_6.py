

from math import *

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    g = abs(a[0])
    for i in range(1, n):
        g = gcd(g, abs(a[i]))
    print(g)

main()
