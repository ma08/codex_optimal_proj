

import sys

def main():
    a, b, c, d = [int(x) for x in sys.stdin.readline().split()]
    print(count(a, b, c, d))

def count(a, b, c, d):
    return b - a + 1 - count_divisible_by_c(a, b, c) - count_divisible_by_d(a, b, d) + count_divisible_by_cd(a, b, c, d)

def count_divisible_by_c(a, b, c):
    return (b // c) - ((a - 1) // c)

def count_divisible_by_d(a, b, d):
    return (b // d) - ((a - 1) // d)

def count_divisible_by_cd(a, b, c, d):
    return (b // (c * d)) - ((a - 1) // (c * d))

if __name__ == '__main__':
    main()