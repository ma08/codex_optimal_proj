
import sys

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b//gcd(a, b)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(lcm(a[0], a[1]))

if __name__ == '__main__':
    main()
