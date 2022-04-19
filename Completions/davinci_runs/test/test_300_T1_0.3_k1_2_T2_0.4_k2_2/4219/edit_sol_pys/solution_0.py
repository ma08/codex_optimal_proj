

import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    print(solve(N, M, A, B))

def solve(N, M, A, B):
    pass

if __name__ == '__main__':
    main()
