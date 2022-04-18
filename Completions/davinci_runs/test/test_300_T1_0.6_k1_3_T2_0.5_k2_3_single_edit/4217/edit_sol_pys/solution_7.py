
import sys
import math


def main():
    a, b = map(int, sys.stdin.readline().split())
    print(math.ceil(math.sqrt(b)-math.sqrt(a)))


if __name__ == '__main__':
    main()
