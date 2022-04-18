

import sys
import math

def main():
    h, v = map(int, sys.stdin.readline().split())
    print(math.ceil(h / math.sin(math.radians(v))))

if __name__ == '__main__':
    main()