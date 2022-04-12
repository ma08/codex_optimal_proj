import sys
sys.setrecursionlimit(10**6)

from math import sin, asin, sqrt

def main():
    # n = int(input())
    # for i in range(n):
    #     a, b, c = map(int, input().split())
    #     theta = asin(sin(asin(a/c)) + sin(asin(b/c))) # law of sines
    #     L = (sqrt(a**2 + b**2 - 2*a*b*cos(theta)) - a*sin(theta) - b*sin(theta))/2
    #     print(L)
    a = [1, 2, 3]
    b = [4, 5, 6]
    print(a + b)

if __name__ == "__main__":
    main()
