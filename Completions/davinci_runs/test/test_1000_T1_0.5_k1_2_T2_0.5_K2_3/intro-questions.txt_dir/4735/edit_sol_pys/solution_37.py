

import sys
import math

def calc(a, b):
    return math.sqrt(a**2 + b**2)



def main():
    a, b = map(int, sys.stdin.readline().split())
    print(calc(a, b))


if __name__ == '__main__':
    main()
