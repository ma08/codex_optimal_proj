

import sys

def solve(n):
    if n % 2 == 0:
        return 0
    else:
        return 1

def main():
    n = int(sys.stdin.readline().strip())
    print(solve(n))

if __name__ == '__main__':
    main()