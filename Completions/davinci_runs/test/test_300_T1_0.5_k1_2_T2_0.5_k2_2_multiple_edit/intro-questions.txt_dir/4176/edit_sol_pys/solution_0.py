
import sys

def main():
    # input a, b
    a, b = map(int, sys.stdin.readline().split())
    # output lcm(a, b)
    print(lcm(a, b))

def lcm(a, b):
    """
    return lcm(a, b)
    """
    return a * b // gcd(a, b)

def gcd(a, b):
    """
    return gcd(a, b)
    """
    while b:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    main()
