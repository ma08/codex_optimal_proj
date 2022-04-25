

import sys

def main():
    t = int(input())
    for i in range(t):
        a, b, d = map(int, input().split())
        print(calculate(a, b, d))

def calculate(a, b, d):
    res = 0
    while b % a != 0 or d % b != 0:
        if b % a != 0:
            b += 1
            res += 1
        if d % b != 0:
            d += 1
            res += 1
    return res, a, b, d

if __name__ == '__main__':
    main()
