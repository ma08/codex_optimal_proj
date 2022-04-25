import sys

def main():
    # input
    a, b = map(int, sys.stdin.readline().split())
    # output
    print(lcm(a, b))

def lcm(a, b):
    """
    最大公約数を求める
    """
    return a * b // gcd(a, b)

def gcd(a, b):
    """
    最小公倍数を求める
    """
    while b:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    main()
