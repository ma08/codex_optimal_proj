

from sys import stdin
from math import pi

def main():
    line = stdin.readline().split()
    r = float(line[0])
    c = float(line[1])

    cheese = pi * (r**2 - c**2)
    area = pi * r**2

    print(cheese / area)

main()
