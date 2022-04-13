

from sys import stdin, stdout
from math import pi

def main():
    line = stdin.readline().split()
    r = int(line[0])
    c = int(line[1])

    cheese = pi * (r**2 - c**2)
    area = pi * r**2

    stdout.write(str(cheese / area) + "\n")

main()
