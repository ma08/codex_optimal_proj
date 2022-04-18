
from math import pi
import sys

def main():
    R, C = map(int, sys.stdin.readline().split())
    pizza_area = pi * (R ** 2)
    cheese_area = pizza_area - pi * ((R - C) ** 2)
    print(100 * (cheese_area / pizza_area))

if __name__ == "__main__":
    main()
