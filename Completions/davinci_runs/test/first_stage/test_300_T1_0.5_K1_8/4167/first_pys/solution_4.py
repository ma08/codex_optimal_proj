

import sys

def main():
    n,k = map(int, sys.stdin.readline().split())
    print(n**3 - ((n//k)*(n//k)*(n//k)))

if __name__ == '__main__':
    main()