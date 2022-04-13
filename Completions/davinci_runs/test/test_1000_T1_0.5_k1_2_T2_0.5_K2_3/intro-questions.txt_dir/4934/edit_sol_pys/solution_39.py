import sys
import math


def main():
    pass


if __name__ == '__main__':
    main()

h, v = [int(i) for i in sys.stdin.readline().split()]

print(math.ceil(h/math.sin(math.radians(v))))
