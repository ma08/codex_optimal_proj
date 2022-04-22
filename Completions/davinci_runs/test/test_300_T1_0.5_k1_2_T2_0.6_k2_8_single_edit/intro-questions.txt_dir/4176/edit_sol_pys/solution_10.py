
import math
import sys

def main():
    while 1:
        # input
        a, b = map(int, sys.stdin.readline().split())
        # output
        print(lcm(a, b))

def lcm(a, b):
    """
    最小公倍数を求める
    """
    return a * b // gcd(a, b)

def gcd(a, b):
    """
    最大公約数を求める
    """
    return math.gcd(a, b)

if __name__ == '__main__':
    main()
