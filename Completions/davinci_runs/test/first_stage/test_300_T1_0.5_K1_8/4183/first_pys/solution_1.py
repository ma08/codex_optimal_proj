

import math

def gcd(a, b):
    """
    最大公約数
    """
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    最小公倍数
    """
    return a * b // gcd(a, b)

def lcm_list(numbers):
    """
    リスト内の最小公倍数
    """
    return reduce(lcm, numbers)

def main():
    n = int(input())
    t = [int(input()) for i in range(n)]
    print(lcm_list(t))

if __name__ == '__main__':
    main()