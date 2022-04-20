'''
File: gcd.py
Author: Michael Cooper
Description: Calculates the GCD of a list of numbers
'''

import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    g = a[0]
    for i in range(1, n):
        g = gcd(g, a[i])
    print(g)

if __name__ == '__main__':
    main()
