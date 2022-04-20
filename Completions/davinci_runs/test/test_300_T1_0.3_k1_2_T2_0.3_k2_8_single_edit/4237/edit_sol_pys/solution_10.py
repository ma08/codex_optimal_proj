
import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    lcm = c * d // gcd(c, d)
    print((b - a + 1) - (b // c - (a - 1) // c) - (b // d - (a - 1) // d) + (b // lcm - (a - 1) // lcm))


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b

    return a

if __name__ == '__main__':
    main()
