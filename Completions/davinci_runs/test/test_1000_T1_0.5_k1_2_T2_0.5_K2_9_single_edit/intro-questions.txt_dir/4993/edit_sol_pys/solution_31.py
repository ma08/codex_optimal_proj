import math

import sys

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        print(math.ceil((x - 2) / 3) * math.ceil((y - 2) / 3))

if __name__ == '__main__':
    main()
