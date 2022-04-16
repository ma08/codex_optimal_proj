

from sys import stdin
from math import pi

def main():
    line = stdin.readline().split()
    r = int(line[0])
    c = int(line[1])

    cheese = pi * (r*r - c*c)
    area = pi * r*r

    print(cheese / area)

main()
