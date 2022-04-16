
from math import sqrt

def area(a, b, c, d):
    s = (a + b + c + d) / 2
    return sqrt((s - a) * (s - b) * (s - c) * (s - d))

def main():
    side = [int(x) for x in input().split()]
    side.sort()
    print(max(area(side[0], side[1], side[2], side[3]), area(side[0], side[1], side[2], side[0] + side[1] + side[2])))

if __name__ == "__main__":
    main()
