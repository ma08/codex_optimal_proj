

from sys import stdin
from math import pi

def main():
    line = stdin.readline()
    r, c = [int(x) for x in line.split()]

    cheese = pi * (r**2 - c**2)
    area = pi * r**2

    print(cheese / area)

main()
