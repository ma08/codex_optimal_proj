
from math import sqrt, pi, acos

def cos(a, b, c):
    return (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)

def area(a, b, c):
    return a * b * sin(c) / 2

def area_triangle(a, b, c):
    return sqrt(s * (s - a) * (s - b) * (s - c))

def area_trapezoid(a, b, c, d):
    h = area_triangle(a, b, c) / (a - d)
    return (a + d) / 2 * h

def main():
    a, b, c, d = [int(x) for x in input().split()]
    s = (a + b + c + d) / 2
    print(max(area_trapezoid(a, b, c, d), area_trapezoid(a, b, c, a + b + c)))

if __name__ == "__main__":
    main()
