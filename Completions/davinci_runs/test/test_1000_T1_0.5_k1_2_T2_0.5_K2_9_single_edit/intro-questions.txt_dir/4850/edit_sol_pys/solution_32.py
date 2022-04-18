from math import sin, asin, sqrt
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        theta = asin(a/c) + asin(b/c)
        print(sqrt(a**2 + b**2 - 2*a*b*cos(theta))/2)

if __name__ == "__main__":
    main()
