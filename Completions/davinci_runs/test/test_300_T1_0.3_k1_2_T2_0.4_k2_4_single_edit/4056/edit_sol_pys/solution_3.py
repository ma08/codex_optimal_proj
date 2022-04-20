
from math import gcd


def gcd_numbers():
    n = int(input())
    a = [int(i) for i in input().split()]
    g = a[0]
    for i in range(1, n):
        g = gcd(g, a[i])
    print(g)


if __name__ == "__main__":
    gcd_numbers()
