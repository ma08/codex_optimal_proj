

import sys

def main():
    print(solve())

def solve():
    n = int(sys.stdin.readline())
    if n % 2 == 1:
        return n // 2 - 1
    else:
        return n // 2

if __name__ == '__main__':
    main()
