

from sys import stdin
from math import pi

def main():
    r = int(stdin.readline())
    c = int(stdin.readline())

    cheese = pi * (r**2 - c**2)
    area = pi * r**2

    print(cheese / area)

main()
