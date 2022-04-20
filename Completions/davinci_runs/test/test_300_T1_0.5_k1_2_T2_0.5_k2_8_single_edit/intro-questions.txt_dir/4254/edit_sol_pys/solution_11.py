import math

import sys

def main():
    for line in sys.stdin:
        a, b = map(int, line.split())
        print(math.gcd(a, b))

if __name__ == '__main__':
    main()
