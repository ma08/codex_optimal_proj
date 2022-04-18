

import sys

def main():
    n, h, v = map(int, sys.stdin.readline().split())
    print(max((n-h)*(n-v)*4, h*v*4))

if __name__ == "__main__":
    main()
