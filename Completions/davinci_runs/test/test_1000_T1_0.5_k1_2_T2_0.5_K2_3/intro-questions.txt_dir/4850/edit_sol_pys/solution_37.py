import sys

from math import sin, asin, sqrt

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        a, b, c = map(int, sys.stdin.readline().split())
        theta = asin(sin(asin(a/c)) + sin(asin(b/c)))
        l = (sqrt(a**2 + b**2 - 2*a*b*cos(theta)) - a*sin(theta) - b*sin(theta))/2
        print(l)

if __name__ == "__main__":
    main()
