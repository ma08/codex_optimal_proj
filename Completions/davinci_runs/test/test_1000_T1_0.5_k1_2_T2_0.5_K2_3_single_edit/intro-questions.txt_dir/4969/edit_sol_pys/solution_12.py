

from sys import stdin
from math import pi

def main():
    line = stdin.readline().split()
    r = int(line[0])
    c = int(line[2])

    cheese = (r**2 - c**2)
    area = r**2

    print(cheese / area * 100)

main()
