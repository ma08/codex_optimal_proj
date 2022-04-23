import math

import sys

def main():
    a, b, c = map(int,sys.stdin.readline().split())
    print(math.ceil(a/c) * math.ceil(b/c))

if __name__ == '__main__':
    main()
