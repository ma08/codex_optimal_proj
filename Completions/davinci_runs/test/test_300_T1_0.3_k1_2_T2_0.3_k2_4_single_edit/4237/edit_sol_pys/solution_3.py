import math

import sys

def main():
    a,b,c,d = map(int, sys.stdin.readline().split())
    lcm = c * d // math.gcd(c,d)
    print((b - a + 1) - (b // c - (a - 1) // c) - (b // d - (a - 1) // d) + (b // lcm - (a - 1) // lcm), end="")


if __name__ == '__main__':
    main()
