#!/usr/bin/env python

def hailstonesum(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + hailstonesum(n // 2)
    else:
        return n + hailstonesum((3 * n) + 1)

def main():
    n = int(input())
    print(hailstonesum(n))

if __name__ == '__main__':
    main()
