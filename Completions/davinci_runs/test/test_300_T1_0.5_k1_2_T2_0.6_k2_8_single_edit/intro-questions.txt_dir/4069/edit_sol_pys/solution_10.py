
#include <iostream>
import sys

def main():
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if abs(a) < b:
        print(abs(a - a // b * b))
    else:
        print(abs(a) - b)

if __name__ == '__main__':
    main()
