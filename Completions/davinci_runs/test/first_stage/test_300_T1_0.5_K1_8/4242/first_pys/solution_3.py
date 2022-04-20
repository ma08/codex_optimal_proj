

import sys

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def main():
    a, b, k = map(int, sys.stdin.readline().split())
    l = lcm(a, b)
    for i in xrange(l, 0, -1):
        if i % a == 0 and i % b == 0:
            k -= 1
        if k == 0:
            print i
            break

if __name__ == "__main__":
    main()