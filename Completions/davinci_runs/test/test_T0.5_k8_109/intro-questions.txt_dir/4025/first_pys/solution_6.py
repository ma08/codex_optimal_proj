

import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    a, b, c = map(int, sys.stdin.readline().split())

    # The number of days the cat can eat without additional food purchases
    # is the number of days in the smallest period that contains all of the
    # dishes.
    num_days = lcm(a, lcm(b, c))

    print(num_days)

if __name__ == '__main__':
    main()