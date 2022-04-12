

from sys import stdin
from math import pi

def main():
    line = stdin.readline()
    r = int(line)
    line = stdin.readline()
    c = int(line)

    cheese = pi * (r**2 - c**2) # cheese
    area = pi * r**2

    print(cheese / area)

main()
