

import sys


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def gcd_3(a, b, c):
    return gcd(gcd(a, b), c)


def main():
    K = int(sys.stdin.readline())
    ans = 0
    for a in range(1, K + 1):
        for b in range(1, K + 1):
            for c in range(1, K + 1):
                ans += gcd_3(a, b, c)
    print(ans)


if __name__ == '__main__':
    main()