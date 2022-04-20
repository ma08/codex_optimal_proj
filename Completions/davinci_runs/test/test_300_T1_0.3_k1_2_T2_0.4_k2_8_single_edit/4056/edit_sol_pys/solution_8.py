

from math import gcd

def main():
    n = int(input())
    a = [int(i) for i in input().split()][:n]
    g = a[0]
    for i in range(1, n):
        g = gcd(g, a[i])
    print(g)

main()
