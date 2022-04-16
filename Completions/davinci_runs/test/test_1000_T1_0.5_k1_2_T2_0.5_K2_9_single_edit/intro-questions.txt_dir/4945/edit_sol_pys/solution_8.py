

import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    m, sigma = map(int, sys.stdin.readline().split())

    # let x = y, then x + y >= sigma, 2x >= sigma, x >= sigma/2
    # x + y <= m, 2x <= m, x <= m/2
    # x >= 1, y >= 1
    # so we have sigma/2 <= x <= m/2
    # we want the max of x^2 - ax + a
    # derivative is 2x - a
    # 2x - a = 0, x = a/2
    # x^2 - ax + a = (a/2)^2 - a(a/2) + a = a^2/4 - a^2/2 + a = a/2
    # so max rent is a

    print(a)

if __name__ == "__main__":
    main()
