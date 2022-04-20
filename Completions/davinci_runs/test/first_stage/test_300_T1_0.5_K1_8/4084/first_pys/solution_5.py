

import sys
import math

def main():
    n, a, b = map(int, sys.stdin.readline().strip().split())
    if a == b:
        print(n // (a + b) * a)
    else:
        print(int(math.ceil(n / (a + b)) * min(a, b)))

if __name__ == '__main__':
    main()