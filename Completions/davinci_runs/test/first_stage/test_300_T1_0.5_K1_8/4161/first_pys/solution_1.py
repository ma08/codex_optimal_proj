

import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd3(a, b, c):
    return gcd(gcd(a, b), c)

def sum_gcd3(k):
    s = 0
    for a in range(1, k+1):
        for b in range(1, k+1):
            for c in range(1, k+1):
                s += gcd3(a, b, c)
    return s

def main():
    k = int(input())
    print(sum_gcd3(k))

if __name__ == '__main__':
    main()