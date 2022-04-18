

from math import sin, asin, sqrt

def main():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        theta = asin(sin(asin(a/c)) + sin(asin(b/c)))
        L = (sqrt(a**2 + b**2 - 2*a*b*cos(theta)) - a*sin(theta) - b*sin(theta))/2.0
        print(L)

if __name__ == "__main__":
    main()
