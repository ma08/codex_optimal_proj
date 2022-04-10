

from math import gcd
from sys import stdin

def main():
    a, b = map(int, stdin.readline().strip().split())
    if a > b:
        a, b = b, a
    if a == 1:
        return b*4
    if a == b:
        return a*4
    if a == 2:
        return 2*(b-1) + 2*(2*(b//2) + 2)
    if b % a == 0:
        return (b//a)*(a+a+a+a)
    if b // a > 2:
        return a*4 + b*2
    return (a+a) + (b-a)*2

if __name__ == "__main__":
    print(main())