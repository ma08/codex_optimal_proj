
import sys
from math import gcd

def main():
    n = int(sys.stdin.readline())
    a = [int(i) for i in sys.stdin.readline().split()]
    g = a[0]
    for i in range(1, n):
        g = gcd(g, a[i])
    print(g)

main()
