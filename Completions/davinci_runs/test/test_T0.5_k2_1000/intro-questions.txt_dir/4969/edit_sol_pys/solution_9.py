

from sys import stdin
from math import pi

def main():
    line = stdin.readline().split()
    r = int(line[0])
    c = int(line[1])

    cheese = pi * (r**2 - c**2) # cheese
    area = pi * r**2

    print(cheese / area) # print

main()
