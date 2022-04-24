
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    a = int(input())
    b = int(input())
    print(lcm(a,b))

if __name__ == '__main__':
    main()
