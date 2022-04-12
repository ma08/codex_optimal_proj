
from math import sqrt

def area(a, b, c, d):
    s = (a + b + c + d) / 2
    return sqrt((s - a) * (s - b) * (s - c) * (s - d))

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(max(area(a, b, c, d), area(a, b, c, a + b + c)))

if __name__ == "__main__":
    main()
