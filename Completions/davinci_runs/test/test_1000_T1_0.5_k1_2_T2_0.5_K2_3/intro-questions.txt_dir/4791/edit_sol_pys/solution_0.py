
from math import sqrt

def area(a, b, c, d):  # area of trapezoid.
    s = (a + b + c + d) / 2
    return sqrt((s - a) * (s - b) * (s - c) * (s - d))

def main():
    s = [int(x) for x in input().split()]  # input.
    s.sort()  # sort input.
    print(max(area(s[0], s[1], s[2], s[3]), area(s[0], s[1], s[2], s[0] + s[1] + s[2])))  # print answer.

if __name__ == "__main__":
    main()
