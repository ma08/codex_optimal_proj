

import sys
import math

def main():
    a, b = map(int, sys.stdin.readline().split())
    print(math.ceil(a / math.sin(math.radians(b))))

if __name__ == '__main__':
    main()
