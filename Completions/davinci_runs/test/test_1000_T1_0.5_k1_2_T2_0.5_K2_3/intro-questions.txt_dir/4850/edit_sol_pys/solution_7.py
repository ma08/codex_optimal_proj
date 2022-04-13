

from math import sin, asin, sqrt, acos, cos

def main():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        theta = acos(cos(asin(a/c)) + cos(asin(b/c)) - 1)
        L = (sqrt(a**2 + b**2 - 2*a*b*cos(theta)) - a*sin(asin(a/c)) - b*sin(asin(b/c)))/2
        print(L)

if __name__ == "__main__":
    main()
