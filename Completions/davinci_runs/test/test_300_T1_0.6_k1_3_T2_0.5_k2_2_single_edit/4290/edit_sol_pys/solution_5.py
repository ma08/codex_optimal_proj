

import sys

def solve(n, m):
    return n * m

def main():
    n,m = map(int, input().strip().split())
    print(solve(n,m))


if __name__ == '__main__':
    main()
