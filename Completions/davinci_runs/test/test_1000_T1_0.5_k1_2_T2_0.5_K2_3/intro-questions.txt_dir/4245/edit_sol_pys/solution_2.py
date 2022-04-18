
import math


def min_power_strip(a, b):
    return math.ceil(b / a)


def main():
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    print(min_power_strip(a, b))


if __name__ == '__main__':
    main()
