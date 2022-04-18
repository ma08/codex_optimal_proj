import sys
from math import sqrt


def area(s1, s2, s3):
    s = (s1 + s2 + s3) / 2.0
    return sqrt((s - s1) * (s - s2) * (s - s3))
    

def main():
    s1, s2, s3 = map(int, sys.stdin.readline().split())
    print(area(s1, s2, s3))


if __name__ == "__main__":
    main()
