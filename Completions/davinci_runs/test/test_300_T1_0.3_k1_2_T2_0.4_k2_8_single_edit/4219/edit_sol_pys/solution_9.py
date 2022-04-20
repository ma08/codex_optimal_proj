
import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    S = list(map(int, sys.stdin.readline().split()))
    T = list(map(int, sys.stdin.readline().split()))
    print(solve(N, M, S, T))

def solve(N, M, S, T):
    return 0


if __name__ == '__main__':
    main()
