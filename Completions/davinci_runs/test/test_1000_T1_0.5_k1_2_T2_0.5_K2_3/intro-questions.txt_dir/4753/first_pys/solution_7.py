

import sys

def solve(n):
    return n*(n-3)//2

def main():
    n = int(sys.stdin.readline())
    print(solve(n))

if __name__ == '__main__':
    main()