

import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    print((b//a)+(b%a!=0))

if __name__ == "__main__":
    main()
