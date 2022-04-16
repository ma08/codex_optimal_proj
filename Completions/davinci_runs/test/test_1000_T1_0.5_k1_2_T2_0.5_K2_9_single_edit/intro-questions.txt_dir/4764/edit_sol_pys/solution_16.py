

import sys

def main():
    n, h, v = map(int, sys.stdin.readline().split())
    print((n-h)*(n-v)*4) 

if __name__ == "__main__":
    main()
