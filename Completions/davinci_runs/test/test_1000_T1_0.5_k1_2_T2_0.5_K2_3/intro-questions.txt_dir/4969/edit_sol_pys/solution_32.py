

from sys import stdin
from math import pi

def main():
    line = stdin.readline().split()  # read input
    r = int(line[0])  # radius
    c = int(line[1])  # hole radius

    cheese = pi * (r**2 - c**2)  # area of cheese
    area = pi * r**2

    print(cheese / area)

main()
