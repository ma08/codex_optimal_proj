

import sys

def main():
    a, b, c = map(int, sys.stdin.readline().split())
    print(min(a+b+c, a+b+c+a, a+b+c+a+b, 2*a+2*b+2*c))

if __name__ == "__main__":
    main()
