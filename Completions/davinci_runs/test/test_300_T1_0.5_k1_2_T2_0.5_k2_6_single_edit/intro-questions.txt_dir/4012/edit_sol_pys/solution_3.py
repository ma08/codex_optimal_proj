

import sys

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        a, b, c = map(int, sys.stdin.readline().split())
        print(calculate(a, b, c))

def calculate(a, b, c):
    res = 0
    while b % a != 0 or c % b != 0:
        if b % a != 0:
            b += 1
            res += 1
        if c % b != 0:
            c += 1
            res += 1
    return (res, a, b, c)

if __name__ == '__main__':
    main()
