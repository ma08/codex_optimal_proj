

import sys

def main():
    n = int(sys.stdin.readline())
    print(solve(n)) # print() is a function in python 3, not a statement.

def solve(n):
    if n % 2 == 0:
        return n // 2 - 1
    else:
        return n // 2

if __name__ == '__main__':
    main()
