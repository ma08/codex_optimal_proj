
from math import sqrt

def area(a, b, c, d):
    s = (a + b + c + d) / 2
    return sqrt((s - a) * (s - b) * (s - c) * (s - d))

def main():
    s = [float(x) for x in input().split()]
    s.sort()
    print(max(area(s[0], s[1], s[2], s[3]), area(s[0], s[1], s[2], s[0] + s[1] + s[2])))

if __name__ == "__main__":
    main()
