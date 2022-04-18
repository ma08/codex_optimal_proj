

from sys import stdin
from math import pi

def main():
    lines = stdin.readlines()
    for line in lines:
        r, c = map(int, line.split())
        cheese = pi * (r**2 - c**2)
        area = pi * r**2

        area = pi * r**2
        print(cheese / area)

if __name__ == '__main__':
    main()
