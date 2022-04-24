
from fractions import gcd
import sys

def main():
    # input
    a, b = map(int, sys.stdin.readline().split())
    # output
    print(lcm(a, b))

def lcm(a, b):
    """
    最小公倍数を返す
    """
    return a * b // gcd(a, b)

if __name__ == '__main__':
    main()
