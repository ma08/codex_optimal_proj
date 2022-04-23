
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    a, b = [int(i) for i in input().split()]
    print(a * b // gcd(a, b))

if __name__ == '__main__':
    main()
