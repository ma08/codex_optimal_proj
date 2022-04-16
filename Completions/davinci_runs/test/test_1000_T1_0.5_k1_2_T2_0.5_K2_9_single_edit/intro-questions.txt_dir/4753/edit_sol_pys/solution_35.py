

import sys

def solve(n):
    return n*(n-3)//2 # fix syntax errors

def main():
    n = int(sys.stdin.readline())
    print(solve(n))

if __name__ == '__main__':
    main()
